# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, get_list_or_404

# Create your views here.
from .models import Image, Tag

# /images/
def index(request, lang=''):
	#set default behaviour
	err=''
	if lang=='':
		lang='en'
	elif not (lang=='en' or lang=='no' or lang=='jp'):
		lang='en'
		err='Language does not exists! Showing default!\n' 

	tags = Tag.objects.filter(tag='pr')
	photo_list = get_list_or_404(Image, tags__in=tags)
	context = {	'photo_list': photo_list, 'err': err, 'cat': 'preview' }
	page = 'images/index_' + lang + '.html'
	return render(request, page, context)

#/images/[cat]/[lang]
def selection(request, cat='', lang=''):
	err=''
	#set default behaviour
	cat_short = {
		'': lambda x: 'pr',
		'preview': lambda x: 'pr',
		'nature': lambda x: 'na',
		'people': lambda x: 'pe',
		'urban': lambda x: 'ur',
		'other': lambda x: 'ot'
	}[cat](lambda x: '')

	if not (cat_short=='pr' or cat_short=='pe' or cat_short=='na' or cat_short=='ur' or cat_short=='ot'):
		err+='Category ' + cat + ' does not exists! Showing default!\n'
		cat_short='pr'

	if lang=='':
		lang='en'
	elif not (lang=='en' or lang=='no' or lang=='jp'):
		lang='en'
		err+='Language does not exists! Showing default!\n' 

	tags = Tag.objects.filter(tag=cat_short)
	photo_list = get_list_or_404(Image, tags__in=tags)
	context = {	'photo_list': photo_list, 'err': err, 'cat': cat }
	page = 'images/index_' + lang + '.html'
	return render(request, page, context)