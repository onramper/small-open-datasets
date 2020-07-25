import pandas as pd
import re
from PIL import Image, ImageDraw, ImageFont
import base64
from io import BytesIO
import json

def remove_citations(x):
    return re.sub(r'\[.{1,2}\]', '', str(x)).replace('\u200a', '')

def generate_table(url):
    table = pd.read_html(url)[0]
    table = table.applymap(remove_citations)
    table.rename(columns=remove_citations, inplace=True)
    return table

def clean_country_table(table):
    return table.applymap(lambda x: re.sub(r' – See .*', '', x))

fonts = {}
for i in range(1, 41):
    fonts[i] = ImageFont.truetype("./NotoSans2-Regular.ttf", i)

def build_icon(symbol, code):
    W, H = (50,50)
    img = Image.new('RGBA', (W, H), (255,255,255,0))
    draw = ImageDraw.Draw(img)
    for size in range(40, 0, -1):
        fnt=fonts[size]
        w, h = draw.textsize(symbol, font=fnt)
        if w < W:
            break
    draw.text(((W-w)/2,(H-h-5)/2), symbol, font=fnt, fill=(0,0,0, 255), align='center')
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    #img.save(code+'.png')
    return "data:image/png;base64," + base64.b64encode(buffered.getvalue()).decode("utf-8") 

currency_url = "https://en.wikipedia.org/wiki/List_of_circulating_currencies#List_of_circulating_currencies_by_state_or_territory"
currency_table = generate_table(currency_url) 

currencies = {}
for i in range(len(currency_table)):
    symbol = currency_table['Symbol orAbbrev.'][i]
    iso_code = currency_table['ISO code'][i]
    name = currency_table['Currency'][i]
    if symbol == "(none)" or iso_code == "(none)" or name == "(none)":
        continue
    if " or " in symbol:
        symbol = symbol.split(' or ')[-1]
    icon = build_icon(symbol, iso_code)
    currencies[iso_code] = { "name":name, "icon":icon }

open("index.js", "w+").write("module.exports = " + json.dumps(currencies))
