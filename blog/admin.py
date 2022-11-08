from django.contrib import admin
from blog.models import AutosNuevo, AutosUsado, Avatar, MotosNueva, MotosUsada

# Registr your models here.

admin.site.register(AutosNuevo)
admin.site.register(AutosUsado)
admin.site.register(MotosNueva)
admin.site.register(MotosUsada)
admin.site.register(Avatar)
