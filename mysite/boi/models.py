from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.
class Mercadoria(models.Model):
    TYPE_CHOICES = (
        ('Compra', 'Compra'),
        ('Venda', 'Venda'),)
    codigo = models.IntegerField()
    tipo_mercadoria =models.CharField(max_length=20, null=True, blank=True)
    nome = models.CharField(max_length=30, null=True, blank=True)
    quantidade = models.IntegerField()
    preco = models.CharField(max_length=10)
    tipo_negocio =models.CharField(max_length=20, null=True, blank=True,choices=TYPE_CHOICES)
    def __str__(self):
        return self.nome
    def was_published_recently(self):
        now = timezone.now()




class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username