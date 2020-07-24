# base64-cryptocurrency-icons
> A collection of base64-encoded cryptocurrency icons

## Introduction
This module just provides a base64-encoded version of the icons provided by [coingecko](https://www.coingecko.com/), updated weekly by a CI job and packaged into js to improve usability and speed (there's no need to read files from disk after the initial loading).

Currently the package present on npm only includes the first 500 cryptocurrencies (ordered by marketcap) to keep package size low, but if you'd like to have access to the 7,000+ cryptocurrencies on coingecko just change the constants on `build.ts`.

## Usage
```js
const icons = require('base64-cryptocurrency-icons');

console.log(icons["btc"]);
{
  "name": "Bitcoin",
  "icon": "data:image/png;base64,iVBORw0KGgoAAAANSUhE..."
}
```

## Features
- Uncompressed size: ~1.6 MB
- Compressed size: ~1.1 MB
- Native Typescript types
- Tracks [coingecko icons](https://coingecko.com/) through a daily CI job
- Automatic npm package publication that keeps it always up to date
- Zero dependencies
- Compatible with all versions of node since 0.12 (released in february 2015)

## License
MIT

## Acknoledgements
Huge thanks to coingecko for leaving their API open and acessible by everyone.
