# base64-cryptocurrency-icons
> A collection of base64-encoded cryptocurrency icons

## Introduction
This module just provides a base64-encoded version of the icons present in [spothq/cryptocurrency-icons](https://github.com/spothq/cryptocurrency-icons), updated daily by a CI job and packaged into js to improve usability and speed (there's no need to read files from disk after the initial loading).

## Usage
```js
const icons = require('base64-crypto-icons');

console.log(icons["BTC"]);
{
  "name": "Bitcoin",
  "color": "#f7931a",
  "icon": "data:image/svg+xml;base64,PHN2ZyB4bWxu..."
}
```

## Features
- Uncompressed size: ~850 kB
- Compressed size: ~300 kB
- Includes Typescript types
- Tracks [spothq/cryptocurrency-icons](https://github.com/spothq/cryptocurrency-icons) through a daily CI job
- Automatic npm package publication, it will always be up-to-date

## License
MIT
