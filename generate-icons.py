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

def new_image():
    img = Image.new('RGBA', (W, H), (255,255,255,0))
    draw = ImageDraw.Draw(img)
    return (img, draw)

def normalize_symbol(symbol):
    if " or " in symbol:
        return symbol.split(' or ')[-1]
    else:
        return symbol

W, H = (50,50)
def get_max_fontsize(fontsize, symbol):
    img, draw = new_image()
    for size in range(fontsize, 0, -1):
        font=fonts[size]
        w, h = draw.textsize(symbol, font=font)
        if w < W:
            return size

def get_char_measurements(symbol, font):
    img, draw = new_image()
    draw.text((0,0), symbol, font=font, fill=(0,0,0, 255), align='center')
    (left, upper, right, lower) = img.getbbox()
    offset_x = left
    offset_y = upper
    w = right - left
    h = lower - upper
    return offset_x, offset_y, w, h

def build_icon(symbol, code, font):
    img, draw = new_image()
    offset_x, offset_y, w, h = get_char_measurements(symbol, font)
    draw.text(((W-w)/2 - offset_x,(H-h)/2 - offset_y), symbol, font=font, fill=(0,0,0, 255), align='center')
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img.save('icons/' +code+'.png')
    return "data:image/png;base64," + base64.b64encode(buffered.getvalue()).decode("utf-8") 

currency_url = "https://en.wikipedia.org/wiki/List_of_circulating_currencies#List_of_circulating_currencies_by_state_or_territory"
currency_table = generate_table(currency_url) 

max_fontsize = 40
for symbol in currency_table['Symbol orAbbrev.']:
    if symbol == "(none)":
        continue
    symbol = normalize_symbol(symbol)
    max_fontsize = get_max_fontsize(max_fontsize, symbol)

currencies = {}
for i in range(len(currency_table)):
    symbol = currency_table['Symbol orAbbrev.'][i]
    iso_code = currency_table['ISO code'][i]
    name = currency_table['Currency'][i]
    if symbol == "(none)" or iso_code == "(none)" or name == "(none)":
        continue
    symbol = normalize_symbol(symbol)
    icon = build_icon(symbol, iso_code, fonts[max_fontsize])
    currencies[iso_code] = { "name":name, "icon":icon, "symbol":symbol }

open("index.ts", "w+").write("export = " + json.dumps(currencies) + " as {[symbol:string]:{name:string, icon:string, symbol:string}|undefined}")
