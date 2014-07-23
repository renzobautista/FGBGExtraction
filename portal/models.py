from django.db import models

# Create your models here.


class Image(models.Model):
	img = models.ImageField(upload_to="3DMeBeta3DEngine/Engine/Input")
	mask = models.ImageField(upload_to="3DMeBeta3DEngine/Engine/Input", blank=True, null=True)
	gif = models.ImageField(upload_to="3DMeBeta3DEngine/Engine/Gif", blank=True, null=True)

	def __str__(self):
		return str(self.img)