# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tag(models.Model):
	TAG_OPTS = (
		('pr', 'Preview'),
		('na', 'Nature'),
		('pe', 'People'),
		('ur', 'Urban'),
		)
	tag = models.CharField(max_length=2, choices=TAG_OPTS)

	def __str__(self):
		return self.tag

class Image(models.Model):
	id = models.AutoField(primary_key=True)
	date = models.DateField(help_text="Select date taken")
	name_no = models.CharField(max_length=30)
	comment_no = models.TextField()
	name_en = models.CharField(max_length=30)
	comment_en = models.TextField()
	name_jp = models.CharField(max_length=30)
	comment_jp = models.TextField()
	tags = models.ManyToManyField(Tag, help_text="Select tag for this picture")
	
	def __str__(self):
		tags = ' / '.join([i.get_tag_display() for i in self.tags.all()])
		return "ID: " + str(self.id) + " Name: " + self.name_en + " Tags: " +  tags

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