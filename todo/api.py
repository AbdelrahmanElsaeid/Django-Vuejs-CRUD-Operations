from .serializers import ToDoSerializer
from .models import ToDo
import pstats
from rest_framework import viewsets





class ToDAPIViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

