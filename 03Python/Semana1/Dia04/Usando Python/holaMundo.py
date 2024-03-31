from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Página de inicio
@app.route('/')
def index():
    return '¡Hola, mundo! Esta es la página de inicio.'

# Página de contacto
@app.route('/contacto', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Recibir los datos del formulario de contacto
        nombre = request.form['nombre']
        mensaje = request.form['mensaje']
        
        # Aquí podrías guardar el mensaje en una base de datos, enviar un correo electrónico, etc.
        
        # Redirigir al usuario de vuelta a la página de inicio después de enviar el mensaje
        return redirect(url_for('index'))
    else:
        # Si el método es GET, mostrar el formulario de contacto
        return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)
