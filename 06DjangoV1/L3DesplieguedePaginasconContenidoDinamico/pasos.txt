# L3Proyecto

# Crear un entorno virtual
python -m venv env_myproject

# Activar el entorno virtual (en Windows)
cd env_myproject 
Scripts\activate

# Volver a carpeta principal
cd ..

# Instalar Django
pip install django

# Crear proyecto Django
django-admin startproject myproject

# entrar al proyecto
cd myproject

# Crear aplicacion Django
python manage.py startapp myfirstapp

# Agregar nuestra nueva app a Settings.py
# ejemplo
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myfirstapp',
]

# Crear migraciones para la nueva aplicacion
python manage.py makemigrations myfirstapp

# Aplicar las migraciones
python manage.py migrate

# Editar el archivo models.py en la carpeta myfirstapp
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
# Crear migracion con cambios en myfirstapp
python manage.py makemigrations myfirstapp

# Cargar a base de datos
python manage.py migrate

# Crear super usuario
python manage.py createsuperuser

# Ejemplo de super usuario
Username (leave blank to use 'basti'): bastian
Email address: bastian@gmail.com
Password: admin1234
Password (again): admin1234
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

# Actualizar en myfirstapp el archivo admin.py
from django.contrib import admin
from .models import Question

admin.site.register(Question)

# Iniciar mi aplicacion
python manage.py runserver

# Abrimos nuestro admin e ingresamos datos

# Cerramos nuestra App
control + c

# Modificamos en myfirstapp el archivo views.py
from django.http import HttpResponse
from django.template import loader

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('myfirstapp/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("Estas buscando una pregunta %s." % question_id)

def results(request, question_id):
    response = "Estas buscando el resultado de una pregunta %s."
    return HttpResponse(response % question_id)
 
def vote(request, question_id):
    return HttpResponse("tu estas votando por una pregunta %s." % question_id)

# Crear carpeta templates en myfirstapp
mkdir myfirstapp/templates

# Crear carpeta myfirstapp en templates
mkdir myfirstapp/templates/myfirstapp

# Crear archivo HTML en myfirstapp/templates/myfirstapp
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}

# Modificar el archivo urls.py de myproject
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('myfirstapp/', include('myfirstapp.urls')),
    path('admin/', admin.site.urls),
]

# Crear el archivo urls.py en myfirstapp
from django.urls import path
from . import views

urlpatterns = [
    # ex: /myfirstapp/
    path('', views.index, name='index'),
    # ex: /myfirstapp/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /myfirstapp/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /myfirstapp/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

# Descargar template "blog" de bootstrap
# Link de descarga
# https://getbootstrap.com/docs/5.3/examples/
# Tomar la carpeta blog y assets
# De blog tomar index.html y pegarlo en myfirstapp/templates/myfirstapp/ el archivo index.html existente lo renombraremos para no perder el archivo original ejemplo index2.html
# Luego crear una carpeta llamada Static y dentro crear una carpeta llamada myfirstapp e insertar la carpeta assets y los archivos de blog blog.css blog.rtl.css

# En el archivo Settings.py agregar la ruta a los archivos estaticos
# Ejemplo 
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'myfirstapp' / 'static' / 'myfirstapp' / 'assets',
    BASE_DIR / 'myfirstapp' / 'static' / 'myfirstapp',
]

# Modificar el index.html para que llame a las rutas de la forma correcta
# Primero agregar en la primera linea
{% load static %}

# Modifica las lineas que llaman a los archivos staticos
# Ejemplo
<link href="{% static 'assets/dist/css/bootstrap.min.css' %}" rel="stylesheet">
<link href="{% static 'blog.css' %}" rel="stylesheet">
<script src="{% static 'assets/dist/js/bootstrap.bundle.min.js' %}"></script>

# Ejecutar el proyecto
python manage.py runserver
