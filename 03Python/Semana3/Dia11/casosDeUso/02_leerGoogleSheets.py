# Importamos la biblioteca pandas y la renombramos como pd para abreviar el código.
import pandas as pd

# Definimos una función llamada leer_sheet_publica que lee los datos de una hoja pública de Google Sheets.
def leer_sheet_publica(sheet_id, sheet_name):
    # Construimos la URL para acceder a la hoja de cálculo en formato CSV utilizando el ID de la hoja y el nombre de la hoja.
    url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
    
    # Utilizamos pd.read_csv() para leer los datos desde la URL y crear un DataFrame de pandas.
    df = pd.read_csv(url)
    
    # Imprimimos las primeras filas del DataFrame para mostrar una vista previa de los datos.
    print(df.head())

# ID de la hoja de cálculo de Google Sheets que queremos leer.
sheet_id = '1qa4692UUhrM5xNyEVycAm8uC8j549NpsxUjWyimBN'
# Nombre de la hoja dentro de la hoja de cálculo que queremos leer.
sheet_name = 'personas'

# Llamamos a la función leer_sheet_publica con el ID de la hoja y el nombre de la hoja como argumentos.
leer_sheet_publica(sheet_id, sheet_name)
