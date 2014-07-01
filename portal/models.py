from django.db import models

# Create your models here.


class Image(models.Model):
	img = models.ImageField(upload_to="imgs")
	mask = models.ImageField(upload_to="masks", blank=True, null=True)

	def __str__(self):
		return str(self.img)