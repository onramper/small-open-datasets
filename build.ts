import { promises as fs } from 'fs';
import fetch from 'node-fetch';

function sleep(seconds: number) {
	return new Promise(resolve => setTimeout(resolve, seconds * 1000));
}

// 50 cryptocurrencies/page
const firstPage = 1;
const maxPage = 10; // Leave as null to get all pages

(async function () {
	let result: {
		[symbol: string]: {
			name: string,
			icon: string,
		}
	} = {};
	const finalResult: typeof result = {};

	let pageOfLastError = firstPage;
	for (let page = firstPage; !(page !== firstPage && Object.keys(result).length !== 0 && page <= maxPage); page++) {
		try {
			result = {};
			const coins = await fetch(`https://api.coingecko.com/api/v3/coins?page=${page}`).then(res => res.json()) as {
				"id": string,
				"symbol": string,
				"name": string,
				"block_time_in_minutes": string,
				"image": {
					"thumb": string,
					"small": string,
					"large": string
				},
				"market_data": any
				"last_updated": string,
				"localization": any
			}[]


			await Promise.all(coins.map(({ symbol, name, image }) => {
				if (!image.small.includes('http')) { // Some crypto don't have associated images (return 'missing_small.png' as in 'supro')
					console.log(`Ignored ${symbol} because no image could be found for it`)
					return Promise.resolve()
				}
				return fetch(image.small).then(res => {
					if (!res.ok) {
						throw new Error(`Couldn't fetch ${symbol} logo`)
					}
					return res.buffer();
				}).then(data => {
					result[symbol] = {
						name,
						icon: "data:image/png;base64," + data.toString('base64')
					}
				})
			}))

			await fs.writeFile(`pages/${page}.json`, JSON.stringify(result));
			Object.assign(finalResult, result);
		} catch (e) {
			// Probably hit the rate limit of 100 requests/min
			if (page !== pageOfLastError) {
				await sleep(60);
				page--;
				pageOfLastError = page;
			} else {
				// If an error happens twice on the same page -> abort
				throw new Error(`Page ${page} triggered two consecutive errors, aborting`)
			}
		}
	}

	await fs.writeFile(`index.ts`, `export = ${JSON.stringify(result)} as {[symbol:string]:{name:string, icon:string}}`);
})()
