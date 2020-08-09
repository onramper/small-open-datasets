from wikipediaTables import remove_citations, generate_table
from PIL import Image, ImageDraw, ImageFont
import base64
from io import BytesIO
import json
from os import listdir, makedirs
from os.path import join
from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode

max_fontsize = 70
fonts = {}
for size in range(1, max_fontsize+1):
    fonts[size] = []
for font_filename in listdir("fonts"):
    font_path = join("fonts", font_filename)
    ttfont = TTFont(font_path)
    for size in range(1, max_fontsize+1):
        fonts[size].append({
            "if":ImageFont.truetype(font_path, size),
            "tt":ttfont
        })

def has_glyph(font, glyph):
    for table in font['cmap'].tables:
        if ord(glyph) in table.cmap.keys():
            return True
    return False

def select_font(fonts, symbol):
    for font in fonts:
        symbol_present = True
        for char in symbol:
            if not has_glyph(font["tt"], char):
                symbol_present = False
                break
        if symbol_present:
            return font["if"]
    print("Couldn't find character "+ symbol +" in any font")
    raise ValueError("Couldn't find character "+ symbol +" in any font")

def new_image(ww, hh):
    img = Image.new('RGBA', (ww, hh), (255,255,255,0))
    draw = ImageDraw.Draw(img)
    return (img, draw)

def normalize_symbol(symbol):
    if " or " in symbol:
        return symbol.split(' or ')[-1]
    else:
        return symbol

W, H = (50,50)
scale_measurements_test = 3
def get_char_measurements(symbol, font):
    img, draw = new_image(W*scale_measurements_test, H*scale_measurements_test)
    draw.text((0,0), symbol, font=font, fill=(0,0,0, 255), align='center')
    (left, upper, right, lower) = img.getbbox()
    offset_x = left
    offset_y = upper
    w = right - left
    h = lower - upper
    return offset_x, offset_y, w, h

scale = 0.7
def get_max_fontsize(symbol):
    for size in range(max_fontsize, 0, -1):
        font=select_font(fonts[size], symbol)
        _, _, w, h = get_char_measurements(symbol, font)
        if w < W*scale and h < H*scale:
            return size

makedirs("icons", exist_ok=True)
def build_icon(symbol, code, font):
    img, draw = new_image(W, H)
    offset_x, offset_y, w, h = get_char_measurements(symbol, font)
    draw.text(((W-w)/2 - offset_x,(H-h)/2 - offset_y), symbol, font=font, fill=(0,0,0, 255), align='center')
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img.save(join('icons', code+'.png'))
    return "data:image/png;base64," + base64.b64encode(buffered.getvalue()).decode("utf-8") 

currency_url = "https://en.wikipedia.org/wiki/List_of_circulating_currencies#List_of_circulating_currencies_by_state_or_territory"
currency_table = generate_table(currency_url) 

'''
for symbol in currency_table['Symbol orAbbrev.']:
    if symbol == "(none)":
        continue
    symbol = normalize_symbol(symbol)
    try:
        max_fontsize = get_max_fontsize(max_fontsize, symbol)
    except:
        continue
'''

currencies = {}
for i in range(len(currency_table)):
    symbol = currency_table['Symbol orAbbrev.'][i]
    iso_code = currency_table['ISO code'][i]
    name = currency_table['Currency'][i]
    if symbol == "(none)" or iso_code == "(none)" or name == "(none)":
        continue
    symbol = normalize_symbol(symbol)
    try:
        size = get_max_fontsize(symbol)
        font = select_font(fonts[size], symbol)
    except:
        continue
    icon = build_icon(symbol, iso_code, font)
    currencies[iso_code] = { "name":name, "icon":icon, "symbol":symbol }

open("index.ts", "w+").write("export = " + json.dumps(currencies) + " as {[symbol:string]:{name:string, icon:string, symbol:string}|undefined}")
