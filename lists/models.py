from django.db import models

class Item(models.Model):
    text = models.TextField(default='')

class List(models.Model):
    pass

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
