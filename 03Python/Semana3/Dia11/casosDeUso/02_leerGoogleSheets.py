import pandas as pd


def leer_sheet_publica(sheet_id, sheet_name):
    url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
    df = pd.read_csv(url)
    print(df.head())


sheet_id = '1qa4692UUhrM5xNyEVycAm8uC8j549NpsxUjWyimBN'
sheet_name = 'personas'
leer_sheet_publica(sheet_id, sheet_name)
