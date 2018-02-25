# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
user= get_user_model()
class User(models.Model):
    iban = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    created_by = models.ForeignKey(user)
    def __str__(self):
        return "%s %s"%(self.first_name,self.last_name)
    class Meta():
        verbose_name_plural = "Users IBAN"