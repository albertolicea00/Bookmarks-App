from django.db import models
from django.contrib.auth.models import User

class Bookmark(models.Model):
    """
    Modelo para almacenar marcadores web.

    Campos:
    - name (str): El nombre del marcador.
    - url (str): La URL del marcador.
    - description (str, opcional): Descripción del marcador.
    - group (ForeignKey a Group): El grupo al que pertenece el marcador.

    Métodos:
    - __str__: Retorna el nombre del marcador como representación en cadena.

    """

    name = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField(blank=True)
    group = models.ForeignKey('BookmarkGroup', on_delete=models.CASCADE, related_name='bookmarks')
    tag = models.ForeignKey('BookmarkTag', on_delete=models.CASCADE, related_name='bookmarks')
    users = models.ManyToManyField(User)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name)


class BookmarkGroup(models.Model):
    """
    Modelo para representar grupos de marcadores web.

    Campos:
    - name (str): El nombre del grupo.
    - icon (str, opcional): Icono asociado al grupo.

    Métodos:
    - __str__: Retorna el nombre del grupo como representación en cadena.

    """

    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True, null=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return str(self.name)

class BookmarkTag(models.Model):
    """
    Modelo para representar etiquetas de marcadores web.

    Campos:
    - name (str): El nombre de la etiqueta.
    - icon (str, opcional): Icono asociado a la etiqueta.

    Métodos:
    - __str__: Retorna el nombre de la etiqueta como representación en cadena.

    """

    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True, null=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return str(self.name)
