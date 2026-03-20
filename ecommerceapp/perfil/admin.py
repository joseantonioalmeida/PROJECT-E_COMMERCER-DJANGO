from django.contrib import admin
from perfil.models import Perfil


# Register your models here.

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    pass