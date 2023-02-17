from .models import Class, Student
from rest_framework import viewsets
from .serializers import ClassSerializer, StudentSerializer


class ClassViewSet(viewsets.ModelViewSet):
    """
    A viewsets for viewing and editing user instances.
    """
    serializer_class = ClassSerializer
    queryset = Class.objects.all()

class StudentViewSet(viewsets.ModelViewSet):
    """
    A viewsets for viewing and editing user instances.
    """
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
