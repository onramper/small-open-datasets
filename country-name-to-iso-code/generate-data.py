from wikipediaTables import remove_citations, generate_table
import json

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
