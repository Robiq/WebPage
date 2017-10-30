# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# /images/
def index(request):
    return HttpResponse("Hello, world. You're at the image index.")
#/images/id
def image(request, id):
	return HttpResponse("You're looking at the page for Picture %s" % id)
#/images/nature
def nature(request):
	return HttpResponse("You're looking for nature pictures!")
#/images/people
def people(request):
	return HttpResponse("You're looking for portrait pictures!")
#/images/urban
def urban(request):
	return HttpResponse("You're looking for urban pictures!")