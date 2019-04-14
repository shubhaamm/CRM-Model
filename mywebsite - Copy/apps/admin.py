from django.contrib import admin
from apps.models import Employee
from apps.models import Employees
from apps.models import Image



# Register your models here.

admin.site.register(Employee)

admin.site.register(Employees)

admin.site.register(Image)
