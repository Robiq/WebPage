# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View

# Create your views here.
from django.http import HttpResponse

#base
class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "prog/index.html", {})

def index(request):
    return HttpResponse("Hello, world. You're at the prog index.")