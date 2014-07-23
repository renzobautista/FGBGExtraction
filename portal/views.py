from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from portal.forms import *
from portal.models import *

from base64 import b64decode
from django.core.files.base import ContentFile

from FGBG import settings
import os
import time

from django.core.files import File

# Create your views here.

def index_view(request):
	data = { 'form' : ImageForm }
	return render(request, 'index.html', data)

def edit_view(request):
	if request.method == "POST":
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			img = Image(img=request.FILES['img'])
			img.save()
			img.fg_img = ContentFile(open(str(img.img.path)), os.path.basename(img.img.name) + '.fg')
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
		params_file = open(settings.MEDIA_ROOT + "/3DMeBeta3DEngine/Engine/Input/Parameters.ini", 'w+')
		params_file.write(params_string(img))
		params_file.close()
		# while not os.path.isfile(settings.MEDIA_ROOT + "/3DMeBeta3DEngine/Engine/Gif" + 'mask' + str(pk) + '.gif'):
		# 	time.sleep(1)
		# fyle = open(settings.MEDIA_ROOT + "/3DMeBeta3DEngine/Engine/Gif" + 'mask' + str(pk) + '.gif')
		# django_file = File(fyle)
		# img.gif.save('new', django_file)
		# fyle.close()
		return HttpResponseRedirect(str(pk))


def params_string(img):
	img_name = os.path.basename(img.img.file.name)
	mask_name = os.path.basename(img.mask.file.name)
	return "[Photo]\nFilename=%s\n\n[Template]\nFilename=%s\n\n[Action]\nCommand1=GIF_150_11_500_500_12\nCommand2=3DTV_600_9_2048_1536\nCommand3=JPG_600\n" % (mask_name, img_name)

def show_view(request, img_id):
	data = { 'img_id' : img_id }
	return render(request, 'show.html', data)
