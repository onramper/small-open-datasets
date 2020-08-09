from wikipediaTables import remove_citations, generate_table
import json

url = "https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes"
country_table = generate_table(url) 

alpha2to3 = {}
alpha3to2 = {}
for i in range(len(country_table)):
    alpha2 = country_table['ISO 3166-1']['Alpha-2 code'][i].replace('.mw-parser-output .monospaced{font-family:monospace,monospace}', '')
    alpha3 = country_table['ISO 3166-1']['Alpha-3 code'][i]
    if alpha2 == alpha3:
        print(f'No code found for {alpha2}, skipping...')
        continue
    if alpha2 == "nan":
        alpha2 = "NA" # When pandas encounters the text 'NA' it interprets it as a nonexisting value aka NaN, correct that
    alpha2=alpha2.lower()
    alpha2to3[alpha2]=alpha3
    alpha3to2[alpha3]=alpha2

tsType = "{[code:string]:string|undefined}"
exports = {"alpha2to3":alpha2to3, "alpha3to2": alpha3to2}
open("index.ts", "w+").write(f'export = {json.dumps(exports)} as {{alpha2to3:{tsType}, alpha3to2:{tsType}}}')

