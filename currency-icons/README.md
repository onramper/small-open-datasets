# Currency Icons
> Icons for all circulating currencies in the world, generated from Wikipedia data. Now with automatic weekly updates!

## Samples
| Code | Name                          | Symbol | Icon |
|------|-------------------------------|--------|------|
| GBP  | British pound                 | £      | ![pound](./samples/GBP.png) |
| EUR  | Euro                          | €      | ![](./samples/EUR.png)     |
| CZK  | Czech koruna                  | Kč     | ![](./samples/CZK.png)     |
| ANG  | Netherlands Antillean guilder | ƒ      | ![](./samples/ANG.png)     |
| NPR  | Nepalese rupee                | रू      | ![](./samples/NPR.png)     |

## Sources
- Currency data comes from [this wikipedia page](https://en.wikipedia.org/wiki/List_of_circulating_currencies).
- Icons are generated using the Noto Sans Light font.

## Generate
```bash
poetry install
npm install
npm run build
```

## Use
```js
import icons from 'currency-icons';

console.log(icons["GBP"])
{
  "name": "British pound",
  "symbol": "£",
  "icon": "data:image/png;base64,iVBORw0KGgoAAAANS..."
}
```

## Why use this package
- Others are not up-to-date or are incorrect
- This is the only package that provides images, this is important because if you display currency symbols directly to your users, some of the currency symbols will be displayed as tofu (those ugly boxes) because the end user isn't using a font that supports those glyphs.

## License
- Currency symbols come from wikipedia and are under the [Creative Commons Attribution-ShareAlike 3.0 Unported License](https://creativecommons.org/licenses/by-sa/3.0/).
- Icons are generated using the Noto font, which is under the [SIL Open Font License (OFL)](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL)
, that has been approved by both OSI and FSF and permits free use, modification and distribution of the font or derived products.
