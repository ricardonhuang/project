from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Passage(models.Model):
    title = models.CharField(max_length=100)
    classifytag = models.CharField(max_length=30)
    text = models.TextField()
    pub_time = models.DateTimeField()
    mod_time = models.DateTimeField()
    def __unicode__(self):
        return  self.title
    
