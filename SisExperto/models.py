from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Enfermedad(models.Model):
	nombre = models.CharField(primary_key=True, max_length=20)

	def __unicode__(self):
		return unicode(self.nombre) or u''

class Sintoma(models.Model):
	descripcion = models.CharField(primary_key=True,max_length=30)

	def __unicode__(self):
		return unicode(self.descripcion) or u''

class SintomaEnfermedad(models.Model):
	ID = models.AutoField(primary_key=True)
	sintoma = models.ForeignKey('Sintoma', on_delete=models.CASCADE)
	enfermedad = models.ForeignKey('Enfermedad', on_delete=models.CASCADE)

	def __unicode__(self):
		return unicode(self.sintoma) + " -> " + unicode(self.enfermedad) or u''