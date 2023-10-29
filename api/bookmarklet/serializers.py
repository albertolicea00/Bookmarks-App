from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (   
    Bookmark,
    BookmarkGroup,
    BookmarkTag
)

class BookmarkSerializer(serializers.ModelSerializer):
    """
    Serializer para convertir objetos Bookmark en representaciones JSON y viceversa.

    Campos:
    - Todos los campos del modelo Bookmark.

    """
    class Meta:
        model = Bookmark
        fields = '__all__'

class BookmarkGroupSerializer(serializers.ModelSerializer):
    """
    Serializer para convertir objetos Group en representaciones JSON y viceversa.

    Campos:
    - Todos los campos del modelo Group.

    """
    class Meta:
        model = BookmarkGroup
        fields = '__all__'

class BookmarkTagSerializer(serializers.ModelSerializer):
    """
    Serializer para convertir objetos Tag en representaciones JSON y viceversa.

    Campos:
    - Todos los campos del modelo Tag.

    """
    class Meta:
        model = BookmarkTag
        fields = '__all__'
