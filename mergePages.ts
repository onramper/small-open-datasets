import { promises as fs } from 'fs';

const firstPage = 1;
const lastPage = 10;

(async function () {
	let result: {
		[symbol: string]: {
			name: string,
			icon: string,
		}
	} = {};

	for (let page = firstPage; page <= lastPage; page++) {
		Object.assign(result, JSON.parse(await fs.readFile(`pages/${page}.json`, 'utf-8')))
	}
	
	await fs.writeFile(`index.ts`, "export = " + JSON.stringify(result) + " as {[symbol:string]:{name:string, icon:string}}");
})()
