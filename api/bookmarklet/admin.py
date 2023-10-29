from django.contrib import admin
from .models import (
    Bookmark,
    BookmarkGroup,
    BookmarkTag
)

class BookmarkAdmin(admin.ModelAdmin):
    """
    Clase de administración para el modelo Bookmark.

    Permite gestionar y mostrar los marcadores web en el panel de administración de Django.

    Atributos:
    - list_display: Define las columnas que se mostrarán en la lista de marcadores.
    - filter_horizontal: Permite gestionar usuarios asociados al marcador.

    """
    list_display = ('name', 'url', 'group', 'tag')
    filter_horizontal = ('users',)

class BookmarkGroupAdmin(admin.ModelAdmin):
    """
    Clase de administración para el modelo BookmarkGroup.

    Permite gestionar y mostrar los grupos de marcadores web en el panel de administración de Django.

    Atributos:
    - list_display: Define las columnas que se mostrarán en la lista de grupos.
    - filter_horizontal: Permite gestionar usuarios asociados al grupo.

    """
    list_display = ('name', 'icon')
    filter_horizontal = ('users',)

class BookmarkTagAdmin(admin.ModelAdmin):
    """
    Clase de administración para el modelo BookmarkTag.

    Permite gestionar y mostrar las etiquetas de marcadores web en el panel de administración de Django.

    Atributos:
    - list_display: Define las columnas que se mostrarán en la lista de etiquetas.
    - filter_horizontal: Permite gestionar usuarios asociados a la etiqueta.

    """
    list_display = ('name', 'icon')
    filter_horizontal = ('users',)


# Registrar los modelos y clases de administración en el panel de administración
admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(BookmarkGroup, BookmarkGroupAdmin)
admin.site.register(BookmarkTag, BookmarkTagAdmin)
