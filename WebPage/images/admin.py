# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Image, Tag

class ImageAdmin(admin.ModelAdmin):
	list_display= ('id', 'name_en', 'comment_en')
	fieldsets = [
	('Date & Tags',	{'fields': ['date', 'tags']}),
	('English', {'fields': ['name_en', 'comment_en']}),
	('Norsk', {'fields': ['name_no', 'comment_no']}),
	('日本語', {'fields': ['name_jp', 'comment_jp']}),
	]

admin.site.register(Image, ImageAdmin)
admin.site.register(Tag)
