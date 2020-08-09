import pandas as pd
import re
from PIL import Image, ImageDraw, ImageFont
import base64
from io import BytesIO
import json
from os import listdir, makedirs
from os.path import join
from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode

def remove_citations(x):
    return re.sub(r'\[.{1,2}\]', '', str(x)).replace('\u200a', '')

def generate_table(url):
    table = pd.read_html(url)[0]
    table = table.applymap(remove_citations)
    table.rename(columns=remove_citations, inplace=True)
    return table

def clean_country_table(table):
    return table.applymap(lambda x: re.sub(r' – See .*', '', x))

url = "https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes"
country_table = generate_table(url) 

countries = []
for i in range(len(country_table)):
    name = country_table['ISO 3166']['Country name'][i]
    official = country_table['Unnamed: 1_level_0']['Official state name'][i]
    alpha2 = country_table['ISO 3166-1']['Alpha-2 code'][i].replace('.mw-parser-output .monospaced{font-family:monospace,monospace}', '')
    alpha3 = country_table['ISO 3166-1']['Alpha-3 code'][i]
    countries.append({ "name":name, "officialName":official, "alpha2":alpha2, "alpha3":alpha3})

open("data.js", "w+").write("export default " + json.dumps(countries))
