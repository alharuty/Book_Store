from django.shortcuts import render, get_object_or_404, redirect
from .models import Book # importamos el modelo Book de models.py
from .forms import formBook # importamos el formulario formBook de forms.py


# creamos nuestras vistas
# son funciones que reciben una petición y devuelven una respuesta
# son la lógica de lo que queremos que haga la aplicación con los datos que le pasemos

# vamos a crear nuestra primera función
def getAllBooks(request): # request es un parametro, que podemos llamarlo como queramos, pero es mejor llamarlo así simepre
    # creamos una variable
    books = Book.objects.all() # obtenemos todos los libros de la base de datos
    
    # render es una función que recibe una petición, un template y un diccionario de datos
    # le decimos que queremos renderizar el template que hay en books/books.html, 
    # y le pasamos los datos que queremos que se muestren en el template
    # ahora iremos a books/templates/books/books.html (modelo/vista/templates (MVT)) y crearemos el template
    # 'libros' es la variable array que creamos para iterar, y books es la variable que hemos creado en la linea 13
    return render(request, 'books/books.html', {'libros': books}) 

def book_details(request, id):
    book = get_object_or_404(Book, pk=id)
    return render(request, 'books/book_details.html', {'book': book})


def createBook(request):
    if request.method == 'POST':
        form = formBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = formBook()
    return render(request, 'books/createbook.html', {'form': form})

def updateBook(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        form = formBook(request.POST, instance=book) #instanciamos el objeto book que ya existía para manipularlo
        if form.is_valid():
            form.save()
            return redirect('/books')
    else:
        form = formBook(instance=book)
    return render(request, 'books/updatebook.html', {'form': form, 'libro': book})