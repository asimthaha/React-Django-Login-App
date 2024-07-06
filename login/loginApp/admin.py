from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(UserRegistrationModel)
class UserRegistrationModelAdmin(admin.ModelAdmin):
    list_display = ("userid","name", "password")
    search_fields = ('name',)