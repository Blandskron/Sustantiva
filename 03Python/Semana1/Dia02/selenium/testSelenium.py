from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Ruta al archivo HTML local
url_html = "http://127.0.0.1:5500/Sustantiva/03Python/Semana1/Dia02/selenium/index.html"

# Configuración del navegador (en este caso, Chrome)
driver = webdriver.Chrome()

try:
    # Abrir el archivo HTML local
    driver.get(url_html)

    # Localizar elementos del formulario por ID
    nombre_input = driver.find_element("id", "nombre")
    email_input = driver.find_element("id", "email")
    mensaje_textarea = driver.find_element("id", "mensaje")
    enviar_button = driver.find_element("xpath", "//input[@type='submit']")

    # Llenar el formulario con datos de ejemplo
    nombre_input.send_keys("Nombre de ejemplo")
    email_input.send_keys("correo@example.com")
    mensaje_textarea.send_keys("Este es un mensaje de ejemplo")

     # Esperar 20 segundos
    time.sleep(20)

    # Enviar el formulario
    enviar_button.click()

finally:
    # Cerrar el navegador al finalizar
    driver.quit()
