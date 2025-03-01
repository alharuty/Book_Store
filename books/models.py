from django.db import models

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

