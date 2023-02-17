from django.contrib import admin
from .models import Class, Student

# Register your models here.

from .models import Student, Class
class ClassAdmin(admin.ModelAdmin):
    list_display =[
        "class_name"
    ]

class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "student_name",
        "roll_no",
        "class_name",
    ]
admin.site.register(Class)
admin.site.register(Student)
