# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
import datetime

class Botiga(models.Model):
    Nif = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    city = models.TextField(default="")
    zipCode = models.TextField(blank=True, null=True)
    stateOrProvince = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    telephone = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('carnisseria:botiga_detail', kwargs={'pk': self.pk})

class Carns(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField('Euro amount', max_digits=8, decimal_places=2, blank=True,null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
    date = models.DateField(default=date.today)
    botiga = models.ForeignKey(Botiga, null=True, related_name='carns', on_delete=models.PROTECT)
    origin = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('carnisseria:carns_detail', kwargs={'pk': self.pk})

class Precuinats(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField('Euro amount', max_digits=8, decimal_places=2, blank=True,null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
    botiga = models.ForeignKey(Botiga, null=True, related_name='precuinats', on_delete=models.PROTECT)
    elaboration_date = models.DateField(default=datetime.date.today)
    caducity_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('carnisseria:precuinats_detail', kwargs={'pk': self.pk})
