# ISO 3166 Alpha Code Converter
> Convert between alpha2 ('us') and alpha3 ('USA') ISO 3166 country codes

## Usage
```js
import { alpha2to3, alpha3to2 } from 'iso3166-alpha-converter'
alpha2to3["us"] // -> "USA"
alpha3to2["USA"] // -> "us"
```

## Development
```bash
# Setup
npm install
poetry install
# Build
npm run build
# Test
npm test
```

## License
Data comes from [this wikipedia page](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) and is licensed under the [Creative Commons Attribution-ShareAlike 3.0 Unported License](https://creativecommons.org/licenses/by-sa/3.0/).
