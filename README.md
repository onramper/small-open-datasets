# currency-icons
All currency data is directly sourced from [this wikipedia page](https://en.wikipedia.org/wiki/List_of_circulating_currencies).

Icons are generated using Noto Sans Light.

## Generate
```bash
poetry install
poetry shell
python generate-icons.py
npm run build
```

## Use
```js
import icons from 'currency-icons';

console.log(icons["GBP"])
{
  "name": "British pound",
  "icon": "data:image/png;base64,iVBORw0KGgoAAAANS..."
}
```

## Why use this package
- Others are not up-to-date or are incorrect
- This is the only package that provides images, this is important because if you display currency symbols directly to your users, some of the currency symbols will be displayed as tofu (those ugly boxes) because the end user isn't using a font that supports those glyphs.
