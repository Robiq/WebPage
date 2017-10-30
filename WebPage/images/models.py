# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Image(models.Model):
	id = models.AutoField(primary_key=True)
	date = models.DateField()
	path = models.CharField(max_length=30)
	name_no = models.CharField(max_length=30)
	name_jp = models.CharField(max_length=30)
	name_en = models.CharField(max_length=30)
	comment_en = models.TextField()
	comment_no = models.TextField()
	comment_jp = models.TextField()
	
	def __str__(self):
		return "ID: " + str(self.id) + " Name: " + self.name_en

	def getLang(self, lang):
		name = ""
		comment = ""
		if lang == "NO":
			name = name_no
			comment = comment_no
		elif lang == "jp":
			name = name_jp
			comment = comment_jp
		else:
			name = name_en
			comment = comment_en
			
		return name, comment

	class Meta:
		ordering = ['id']

class Preview(models.Model):

	class Meta:
		ordering = ['id']

class Nature(models.Model):

	class Meta:
		ordering = ['id']

class People(models.Model):

	class Meta:
		ordering = ['id']

class Urban(models.Model):

	class Meta:
		ordering = ['id']