En este proyecto vamos a utilizar el framework Django para implementar un sistema básico de gestión de libros, monolítico. Es una aplicación web en la que se pueden crear, editar y eliminar libros, lo que se denomina CRUD (Create, Read, Update, Delete). 

Es un proyecto MVC (Modelo-Vista-Controlador), donde:

- **Modelos (Models)** representan la estructura de los datos (libros).
- **Vistas (Views)** manejan la lógica de presentación y recuperan información de los modelos.
- **Controladores (Urls y Forms)** conectan las vistas con las solicitudes del usuario.

NO TIENE ESTILOS.

### Objetivo del proyecto
El objetivo principal es aprender y practicar la creación de aplicaciones Django con funcionalidad CRUD, reforzando el uso de modelos, vistas, formularios y el sistema de administración de Django. También puede servir como base para proyectos más complejos, como una librería en línea o un sistema de gestión de biblioteca.


1. Ir a nuestra carpeta de proyectos.
2. `mkdir book_store` => creamos repositorio de nuestro proyecto
3. `cd book_store` => nos movemos a la carpeta de nuestro proyecto.
4. `uv venv .venv` => creamos entorno virtual.
5. `source .venv/bin/activate` => activamos entorno virtual.
6. `uv init --bare`=> creamos archivo .toml
7. `uv add django` => agregamos django a nuestro entorno virtual y al archivo .toml
8. `dajngo-admin startproject book_manage`=> creamos un **NUEVO PROYECTO** llamado book_manage. Es el contenedor principal que festiona la configuración y configuración global de Django. Todos nuestros archivos y aplicaciones se alojan en este proyecto. También contiene manage.py y settings.py que son archivos de configuración del proyecto.
9. `django-admin startapp books` => creamos una **NUEVA APLICACIÓN** llamada books. Una aplicación es un conjunto de modelos, vistas y plantillas que se utilizan para implementar una funcionalidad específica. Por ejemplo una app para manejar los libros, una app para manejar usuarios, etc.
9. Vamos a book_manage > settings.py > INSTALLED_APPS => agregamos la app `books`.
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'books', # agregamos aquí cada app que creemos
]
```
10. Ir a books > models.py => creamos una clase Book con los campos que queramos.
```python
# creamos un modelo llamado Book
class Book(models.Model):
    title = models.CharField(max_length=250, null=False)
    author = models.CharField(max_length=100)
    description = models.TextField()
    publish_date = models.DateField() # ó .DateTimeField para fecha completa
    isbn = models.CharField(max_length=13, unique=True)
    
# creamos un método para mostrar el nombre del libro en el admin
# se les llama magic methods
# no es obligatorio, pero lo ponemos para verificar que el modleo funciona
def __str__(self):
    return self.title
```
11. `python manage.py makemigrations` => creamos las migraciones. Cada vez que creamos un modelo o lo editamos, hay que hacer makemigrations. Se creará una carpeta llamada *migrations* y en este caso el archivo *0001_initial.py* , donde nos dice los cambios que acabamos de crear. Es como hacer el commit de github.
12. `python manage.py migrate` => creamos las tablas en la base de datos. Es como hacer el push de github.
13. Vamos a admin.py y registramos nuestro modelo creado Book. 
```python
from django.contrib import admin
from .models import Book # importamos el modelo Book de models.py

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'isbn')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('publish_date', 'author')
```
14. `python manage.py createsuperuser` => creamos un usuario admin.
15. `python manage.py runserver` => iniciamos el servidor.
16. Vamos a 127.0.0.1:8000/admin y nos logueamos con el usuario admin creado. Aquí podemos hacer acciones CRUD de admin.
17. Vamos a books > views.py y creamos nuestra primera vista. Las vistas son funciones que reciben una petición y devuelven una respuesta. Segurament en esta funcion queramos renderizar algo y para eso tendremos que crear un template.
Este template irá en la carpeta de la propia app, en este caso en books, y dentro crearemos otra carpeta llamada templates, y ahí crearemos el template.html llamadondole como queramos, en este caso book.html
```python
from django.shortcuts import render
from .models import Book # importamos el modelo Book de models.py

# creamos nuestro view
def getllBooks(request):
    books = Book.objects.all()
    return render(request, 'books/books.html', {'books': books}) 
```
18. En la misma carpeta que estamos (books) creamos una carpeta llamada templates y dentro creamos un archivo llamado book.html
```html
<body>
    <ul>
    {% for libro in libros %}
    <li>{{ libro.title }} - {{ libro.author }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```
Con este codigo estamos recorriendo la lista de libros y mostrando el titulo y el autor de cada libro.
19. Ahora vamos a urls.py de la app books y creamos una ruta para nuestra aplicacion books.
```python
from django.contrib import admin # importamos admin
from django.urls import path # importamos path
from .views import getAllBooks

urlpatterns = [
    path('', getAllBooks, name='books'),
]
```
20. Vamos a book_manage > urls.py y agregamos la ruta de la app books.
21. Ahora podemos ir a la url /admin y crear algún libro, para luego poder listarlos y verlos en la página /books.
22. Vamos a 127.0.0.1:8000/books y veremos la lista de libros.
23. Siguiendo los mismos pasos de la linea17 creamos una nueva vista llamada createBook. Y creamos su respectiva url en templates/books/createbook.html . Y seguimos los pasos 18, 19, 20 y 21 si hace falta.
```python
from .forms import formBook

def createBook(request):
    if request.method == 'POST':
        form = formBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = formBook()
    return render(request, 'books/createbook.html', {'form': form})
```
24. Ahora en la misma carpeta de la aplicación books, creamos un archivo forms.py que va a ser el formulario para crear libros para el punto anterior.
```python
from django import forms
from .models import Book

class formBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'publish_date', 'isbn']
```
