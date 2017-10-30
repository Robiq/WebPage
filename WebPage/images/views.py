# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, get_list_or_404

# Create your views here.
from .models import Image

# /images/
def index(request):
	photo_list = get_list_or_404(Preview)
	context = {	'photo_list': photo_list }
	return render(request, 'images/index.html', context)

#/images/id
def image(request, id):
	im = get_object_or_404(Image, pk=id)
	return render(request, 'images/img.html', {'im': im})

#/images/nature
def nature(request):
	photo_list = get_list_or_404(Nature)
	context = {	'photo_list': photo_list }
	return render(request, 'images/index.html', context)

#/images/people
def people(request):
	photo_list = get_list_or_404(People)
	context = {	'photo_list': photo_list }
	return render(request, 'images/index.html', context)

#/images/urban
def urban(request):
	photo_list = get_list_or_404(Urban)
	context = {	'photo_list': photo_list }
	return render(request, 'images/index.html', context)