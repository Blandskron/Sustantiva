from flask import Flask, jsonify
import json

app = Flask(__name__)

# Ruta para mostrar los usuarios en una tabla HTML
@app.route('/usuarios')
def mostrar_usuarios():
    # Leer los datos de usuarios desde el archivo JSON
    with open('usuarios.json') as file:
        datos_usuarios = json.load(file)

    # Crear una tabla HTML
    tabla_html = '<table border="1">'
    tabla_html += '<tr><th>ID</th><th>Nombre</th><th>Edad</th></tr>'

    # Agregar filas de usuarios a la tabla
    for usuario in datos_usuarios:
        tabla_html += f'<tr><td>{usuario["id"]}</td><td>{usuario["nombre"]}</td><td>{usuario["edad"]}</td></tr>'

    tabla_html += '</table>'

    # Devolver la tabla HTML como respuesta
    return tabla_html

if __name__ == '__main__':
    app.run(debug=True)
