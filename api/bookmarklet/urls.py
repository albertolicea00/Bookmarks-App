from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BookmarkViewSet,
    BookmarkGroupViewSet,
    BookmarkTagViewSet
)

router = DefaultRouter()
router.register(r'bookmarks', BookmarkViewSet)
router.register(r'groups', BookmarkGroupViewSet)
router.register(r'tags', BookmarkTagViewSet)
# router.register(r'users', UserList)

urlpatterns = [
    path('api/', include(router.urls)),
]
