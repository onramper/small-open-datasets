import { promises as fs } from 'fs';

(async function () {
	const manifest = JSON.parse(await fs.readFile('./cryptocurrency-icons/manifest.json', 'utf8')) as {
		symbol: string,
		name: string,
		color: string
	}[];

	const result: {
		[symbol: string]: {
			color: string,
			name: string,
			icon: string,
		}
	} = {};

	await Promise.all(manifest.map(({ symbol, name, color })=>
		fs.readFile("./cryptocurrency-icons/svg/black/" + symbol.toLowerCase() + ".svg").then(data => {
			result[symbol] = {
				name,
				color,
				icon: "data:image/svg+xml;base64," + data.toString('base64')
			}
		})
	))

	await fs.writeFile("index.ts", "export = " + JSON.stringify(result) + " as {[symbol:string]:{color:string, name:string, icon:string}}");
})()
