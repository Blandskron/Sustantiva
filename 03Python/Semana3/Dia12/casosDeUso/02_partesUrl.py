# Importamos la función urlparse del módulo urllib.parse, que nos permite analizar componentes de una URL.
from urllib.parse import urlparse

# Definimos una función llamada obtener_partes_url que analiza una URL y devuelve sus partes principales.
def obtener_partes_url(url):
    # Usamos urlparse para analizar la URL y extraer sus componentes.
    url_data = urlparse(url)
    
    # Creamos un diccionario que contiene las partes principales de la URL.
    partes_url = {
        "protocolo": url_data.scheme,   # El protocolo utilizado en la URL (por ejemplo, "https").
        "dominio": url_data.netloc,     # El nombre de dominio de la URL (por ejemplo, "example.com").
        "ruta": url_data.path,          # La ruta dentro del dominio (por ejemplo, "/onboarding").
        "query_params": url_data.query, # Los parámetros de la consulta de la URL (por ejemplo, "type=student").
        "etiqueta": url_data.fragment   # La etiqueta o fragmento de la URL (por ejemplo, "section1").
    }

    return partes_url

# Definimos una URL de ejemplo.
url = "https://example.com/onboarding?type=student#section1"
# Llamamos a la función obtener_partes_url con la URL de ejemplo y almacenamos el resultado en la variable partes_url.
partes_url = obtener_partes_url(url)
# Imprimimos las partes de la URL para verificar el resultado.
print(partes_url)
