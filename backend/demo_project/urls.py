from django.urls import path, include
from rest_framework import routers

from apps.demo.views import PostViewSet

router = routers.DefaultRouter()
router.register(r'api/posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
]
