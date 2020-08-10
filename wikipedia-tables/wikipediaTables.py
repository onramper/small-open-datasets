import pandas as pd
import re

def remove_citations(x):
    return re.sub(r'\[.{1,2}\]', '', str(x)).replace('\u200a', '')

def generate_table(url):
    table = pd.read_html(url)[0]
    table = table.applymap(remove_citations)
    table.rename(columns=remove_citations, inplace=True)
    return table

def clean_country_table(table):
    return table.applymap(lambda x: re.sub(r' – See .*', '', x))

