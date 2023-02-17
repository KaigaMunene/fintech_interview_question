from rest_framework import serializers
from .models import Student, Class


class ClassSerializer(serializers.ModelSerializer):
    class_name = serializers.CharField()
    
    class Meta:
        model = Class
        fields = ["class_name"]

class StudentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField()
    roll_no = serializers.IntegerField()
    class_name = ClassSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ["name", "roll_no", "class_name"]


    
