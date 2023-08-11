from django.urls import path, include
from rest_framework import routers
from .api import ToDAPIViewSet


router = routers.DefaultRouter()
router.register('todo', ToDAPIViewSet)

app_name='todo'

urlpatterns = [
    path('api/', include(router.urls))
]
