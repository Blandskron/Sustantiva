import requests
from bs4 import BeautifulSoup

# URL del sitio web de noticias
url = 'https://www.bbc.com/news'

# Realizar una solicitud GET al sitio web
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Crear un objeto BeautifulSoup para analizar el contenido HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar todas las etiquetas 'a' que contienen los enlaces a las noticias
    news_links = soup.find_all('a', class_='gs-c-promo-heading')

    # Iterar sobre los enlaces de noticias y extraer el título y la URL
    for link in news_links:
        title = link.text.strip()
        news_url = link['href']
        print(f"Titulo: {title}")
        print(f"URL: {news_url}")
        print("-" * 50)
else:
    print("Error al realizar la solicitud al sitio web de noticias.")

#pip install requests beautifulsoup4
