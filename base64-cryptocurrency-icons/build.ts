import { promises as fs } from 'fs';
import fetch from 'node-fetch';

function sleep(seconds: number) {
	return new Promise(resolve => setTimeout(resolve, seconds * 1000));
}

function base64encode(buf:Buffer):string{
	return "data:image/png;base64," + buf.toString('base64');
}

// 50 cryptocurrencies/page
const firstPage = 1;
const maxPage = 90; // Put a high number to get all pages

(async function () {
	let result: {
		[symbol: string]: {
			name: string,
			icon: string,
		}
	} = {};
	let finalResult: typeof result = {};

	let pageOfLastError = firstPage;
	for (let page = firstPage; (page === firstPage || Object.keys(result).length !== 0) && page <= maxPage; page++) {
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
					result[symbol.toUpperCase()] = {
						name,
						icon: base64encode(data)
					}
				})
			}))

			await fs.writeFile(`pages/${page}.json`, JSON.stringify(result));
			// For cryptocurrencies that have the same symbol only the most popular one (decided by order of inclusion in coingecko's API) is included
			finalResult = {...result, ...finalResult};
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

	finalResult['GENERIC'] = {
		name: "Generic",
		icon: base64encode((await fs.readFile('./generic.png')))
	}
	await fs.writeFile(`index.ts`, `export = ${JSON.stringify(finalResult)} as {[symbol:string]:{name:string, icon:string}|undefined}`);
})()
