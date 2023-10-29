from rest_framework import viewsets, generics
from .models import (
    Bookmark, 
    BookmarkGroup, 
    BookmarkTag
)
from .serializers import (
    BookmarkSerializer,
    BookmarkGroupSerializer,
    BookmarkTagSerializer
)

class BookmarkViewSet(viewsets.ModelViewSet):
    """
    Vista que maneja las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para el modelo Bookmark a través de la API.

    Attributes:
    - queryset: Conjunto de objetos del modelo Bookmark.
    - serializer_class: Clase de serializador utilizada para convertir objetos Bookmark en representaciones JSON y viceversa.

    """
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

class BookmarkGroupViewSet(viewsets.ModelViewSet):
    """
    Vista que maneja las operaciones CRUD para el modelo BookmarkGroup a través de la API.

    Attributes:
    - queryset: Conjunto de objetos del modelo BookmarkGroup.
    - serializer_class: Clase de serializador utilizada para convertir objetos BookmarkGroup en representaciones JSON y viceversa.

    """
    queryset = BookmarkGroup.objects.all()
    serializer_class = BookmarkGroupSerializer

class BookmarkTagViewSet(viewsets.ModelViewSet):
    """
    Vista que maneja las operaciones CRUD para el modelo BookmarkTag a través de la API.

    Attributes:
    - queryset: Conjunto de objetos del modelo BookmarkTag.
    - serializer_class: Clase de serializador utilizada para convertir objetos BookmarkTag en representaciones JSON y viceversa.

    """
    queryset = BookmarkTag.objects.all()
    serializer_class = BookmarkTagSerializer
