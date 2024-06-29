# myapp/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'emails', views.EmailViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
