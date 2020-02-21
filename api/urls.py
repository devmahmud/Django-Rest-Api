from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet

router = routers.DefaultRouter()

router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls))
]
