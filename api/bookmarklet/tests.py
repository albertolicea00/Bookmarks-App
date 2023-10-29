from django.test import TestCase
from django.contrib.auth.models import User
from .models import (
    Bookmark,
    BookmarkGroup,
    BookmarkTag
)


class BookmarkModelTest(TestCase):
    """
    Casos de prueba para el modelo Bookmark.
    """
    def setUp(self):
        self.user1 = User.objects.create(username="usuario1")
        self.user2 = User.objects.create(username="usuario2")
        self.group = BookmarkGroup.objects.create(name="Mi Grupo")
        self.tag = BookmarkTag.objects.create(name="Mi Etiqueta")

        self.bookmark = Bookmark.objects.create(
            name="Mi Marcador",
            url="https://www.example.com",
            group=self.group,
            tag=self.tag
        )

    def test_bookmark_name(self):
        """
        Prueba que el campo 'name' del modelo Bookmark sea correcto.
        """
        bookmark = Bookmark.objects.get(id=self.bookmark.id)
        self.assertEqual(bookmark.name, "Mi Marcador")

    def test_bookmark_url(self):
        """
        Prueba que el campo 'url' del modelo Bookmark sea correcto.
        """
        bookmark = Bookmark.objects.get(id=self.bookmark.id)
        self.assertEqual(bookmark.url, "https://www.example.com")

    def test_bookmark_group(self):
        """
        Prueba que el campo 'group' del modelo Bookmark sea correcto.
        """
        bookmark = Bookmark.objects.get(id=self.bookmark.id)
        self.assertEqual(bookmark.group, self.group)
    
    def test_bookmark_tag(self):
        """
        Prueba que el campo 'tag' del modelo Bookmark sea correcto.
        """
        bookmark = Bookmark.objects.get(id=self.bookmark.id)
        self.assertEqual(bookmark.tag, self.tag)

    def test_bookmark_users(self):
        """
        Prueba que el campo 'users' del modelo Bookmark refleje los usuarios asociados.
        """
        bookmark = Bookmark.objects.get(id=self.bookmark.id)
        self.assertIn(self.user1, bookmark.users.all())
        self.assertIn(self.user2, bookmark.users.all())

class BookmarkGroupModelTest(TestCase):
    """
    Casos de prueba para el modelo BookmarkGroup.
    """
    def test_group_name(self):
        """
        Prueba que el campo 'name' del modelo BookmarkGroup sea correcto.
        """
        group = BookmarkGroup.objects.create(name="Mi Grupo de Prueba")
        self.assertEqual(group.name, "Mi Grupo de Prueba")


class BookmarkTagModelTest(TestCase):
    """
    Casos de prueba para el modelo BookmarkTag.
    """
    def test_tag_name(self):
        """
        Prueba que el campo 'name' del modelo BookmarkTag sea correcto.
        """
        tag = BookmarkTag.objects.create(name="Mi Etiqueta")
        self.assertEqual(tag.name, "Mi Etiqueta")
