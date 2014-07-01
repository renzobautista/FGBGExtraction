from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from portal.forms import *
from portal.models import *

from base64 import b64decode
from django.core.files.base import ContentFile

import subprocess
from FGBG import settings

# Create your views here.

def index_view(request):
	data = { 'form' : ImageForm }
	subprocess.Popen('cd ' + settings.BASE_DIR + '; gitup "testing subprocess and custom bash commands"', shell=True)
	return render(request, 'index.html', data)

def edit_view(request):
	if request.method == "POST":
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			img = Image(img=request.FILES['img'])
			img.save()
			data = { 'img' : img, 'id' : img.id }
			return render(request, 'edit.html', data)
		else:
			return HttpResponseRedirect('/')
	else: 
		return HttpResponseRedirect('/')

def get_mask_view(request):
	if request.method == "POST" or request.is_ajax():
		padding_len = 22
		image_data = b64decode(request.POST['imgdata'][padding_len::])
		pk = int(request.POST['id'])
		img = Image.objects.get(id=pk)
		img.mask = ContentFile(image_data, 'mask' + str(pk) + '.png')
		img.save()

		# subprocess.Popen('cd %s; wine engine.exe %s %s', settings.MEDIA_ROOT, img.img, img.mask, shell=True)

	return HttpResponse('')