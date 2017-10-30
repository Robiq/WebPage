# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, get_list_or_404

# Create your views here.
from .models import Image, Tag

# /images/
def index(request):
	tags = Tag.objects.filter(tag='pr')
	photo_list = get_list_or_404(Image, tags__in=tags)
	context = {	'photo_list': photo_list }
	return render(request, 'images/index.html', context)

#/images/id
def image(request, id):
	im = get_object_or_404(Image, pk=id)
	return render(request, 'images/img.html', {'im': im})

#/images/nature
def nature(request):
	tags = Tag.objects.filter(tag='na')
	photo_list = get_list_or_404(Image, tags__in=tags)
	context = {	'photo_list': photo_list }
	return render(request, 'images/index.html', context)

#/images/people
def people(request):
	tags = Tag.objects.filter(tag='pe')
	photo_list = get_list_or_404(Image, tags__in=tags)
	context = {	'photo_list': photo_list }
	return render(request, 'images/index.html', context)

#/images/urban
def urban(request):
	tags = Tag.objects.filter(tag='ur')
	photo_list = get_list_or_404(Image, tags__in=tags)
	context = {	'photo_list': photo_list }
	return render(request, 'images/index.html', context)