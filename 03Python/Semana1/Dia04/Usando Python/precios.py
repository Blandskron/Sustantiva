import requests
from bs4 import BeautifulSoup

# URL del sitio de comercio electrónico
url = 'https://cl.isadoraonline.com/'

# Realizar una solicitud GET al sitio web
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Crear un objeto BeautifulSoup para analizar el contenido HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar todas las etiquetas que contienen los precios de los productos
    price_tags = soup.find_all('span', class_='price')

    # Iterar sobre las etiquetas de precio y extraer el precio de cada producto
    for tag in price_tags:
        price = tag.text.strip()
        print(f"Precio del producto: {price}")
else:
    print("Error al realizar la solicitud al sitio web de comercio electrónico.")
