from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from .models import *

admin.site.register(Student)
admin.site.register(timeIn)
admin.site.register(timeOut)
