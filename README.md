# currency-icons
All currency data is directly sourced from [this wikipedia page](https://en.wikipedia.org/wiki/List_of_circulating_currencies).

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
