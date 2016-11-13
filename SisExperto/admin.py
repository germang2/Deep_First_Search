from django.contrib import admin
from .models import Sintoma, Enfermedad, SintomaEnfermedad
# Register your models here.
admin.site.register(Sintoma)
admin.site.register(Enfermedad)
admin.site.register(SintomaEnfermedad)