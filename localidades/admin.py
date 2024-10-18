from django.contrib import admin

# Register your models here.
from .models import Estado, Municipio

admin.site.register(Estado)
admin.site.register(Municipio)