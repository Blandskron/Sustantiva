from urllib.parse import urlparse


def obtener_partes_url(url):

    url_data = urlparse(url)
    partes_url = {
        "protocolo": url_data.scheme,
        "dominio": url_data.netloc,
        "ruta": url_data.path,
        "query_params": url_data.query,
        "etiqueta": url_data.fragment
    }

    return partes_url


url = "https://example.com/onboarding?type=student#section1"
partes_url = obtener_partes_url(url)
print(partes_url)
