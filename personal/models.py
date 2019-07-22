# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

Deafult_desc = '''Lorem ipsum dolor sit amet,
agam probatus indoctum cu quo.
Est eu quod rationibus,
nam platonem sententiae no.
Eu mel vero oporteat elaboraret.'''


class Category(models.Model):
    Name = models.CharField(max_length=30)
    @property
    def preview(self):
        first = self.images.last()
        return first.image.url

    def __str__(self):
        return self.Name


class Location(models.Model):
    place = models.CharField(max_length=30)

    def __str__(self):
        return self.place


class Image(models.Model):
    Name = models.CharField(max_length=60)
    description = models.TextField(default=Deafult_desc)
    category = models.ForeignKey(Category, related_name="images")
    location = models.ForeignKey(Location)
    submited = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')

    @property
    def allinfo(self):
        info = {
            'name': self.Name,
            'desc': self.description,
            'image': self.image.url,
            'id': self.id
        }
        return str(info)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self, Name=None, category=None):
        self.Name = Name if Name else self.Name
        self.category = category if category else self.category
        self.save()

    @classmethod
    def get_image_by_id(cls, id):
        return cls.objects.get(pk=id)

    @classmethod
    def search_by_location(cls, search_term):
        image = Image.objects.filter(location__id=search_term).all()
        return image

    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images

    @classmethod
    def search_by_title(cls, search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news

    class Meta:
        ordering = ['submited']
