# base64-cryptocurrency-icons
> A collection of base64-encoded cryptocurrency icons

## Introduction
This module just provides a base64-encoded version of the icons provided by [coingecko](https://www.coingecko.com/), updated weekly by a CI job and packaged into js to improve usability and speed (there's no need to read files from disk after the initial loading).

Currently the package present on npm only includes the first 4500 cryptocurrencies (ordered by marketcap) to keep package size low, but if you'd like to have access to the 7,000+ cryptocurrencies on coingecko just change the constants on `build.ts`.

The package also includes a generic icon that can be accessed as `GENERIC`.

## Usage
```js
const icons = require('base64-cryptocurrency-icons');

console.log(icons["BTC"]);
{
  "name": "Bitcoin",
  "icon": "data:image/png;base64,iVBORw0KGgoAAAANSUhE..."
}
```

## Features
- Native Typescript types
- Tracks [coingecko icons](https://coingecko.com/) through a weekly CI job
- Automatic npm package publication that keeps it always up to date
- Zero dependencies
- Compatible with all versions of node since 0.12 (released in february 2015)

## Development
```
# Setup
npm install
# Generate files
npm run generate
# Run tests
npm test
```
This may take a while, as coingecko's API is rate-limited and the build script throttles itself to stay under the limit.

## License
- All cryptocurrency data and icons come from [coingecko](https://www.coingecko.com/), which provides their data "for free, and as-is without any warranty." ([Source](https://www.coingecko.com/en/api)) under [these Terms of Service](https://www.coingecko.com/en/api_terms), that allow anyone "to charge for your services and products that incorporate or integrates our CoinGecko API". Furthermore, I've directly messaged coingecko about the re-distribution of data in this package and they have given permission to do so.
- The generic icon comes from the repository [spothq/cryptocurrency-icons](https://github.com/spothq/cryptocurrency-icons) and is licensed under the [Creative Commons Zero (CC0) license](https://github.com/spothq/cryptocurrency-icons/blob/master/LICENSE.md).

## Acknoledgements
Huge thanks to coingecko for leaving their API open and acessible by everyone.
