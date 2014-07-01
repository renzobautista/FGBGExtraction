from django import forms
from portal.models import Image

class ImageForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ['img', ]
