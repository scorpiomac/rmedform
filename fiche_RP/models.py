from django.db import models

from django.contrib import admin
from django.db import models


class information(models.Model):
    name = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.CharField(max_length=1000)
    message2 = models.CharField(max_length=1000)


class Person(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)


class multistepformexample(models.Model):
    name = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.CharField(max_length=1000)













from phonenumber_field.modelfields import PhoneNumberField


genre_CHOICES = [
    ('M', 'M.'),
    ('F', 'Mme')
    
]

situation_CHOICES = [
    ('célibataire', 'célibataire'),
    ('marié', 'marié(e)'),
    ('divorcé', 'divorcé(e)'),
    ('Veuf', 'Veuf(ve)')
    
]

class Fiche(models.Model):
    nom= models.CharField(max_length=300,null=True)
    nomDj= models.CharField(max_length=300, unique=False,blank=True)
    prenom= models.CharField(max_length=300, unique=False)
    genre = models.CharField(max_length=1, choices=genre_CHOICES)
    nationalite= models.CharField(max_length=300, unique=False)
    situation = models.CharField(max_length=20, choices=situation_CHOICES)
    birth_date = models.DateField(null=True, blank=False)
    lieu= models.CharField(max_length=300, unique=False)
    fixe=PhoneNumberField(blank=True, unique=False)
    mobile=PhoneNumberField(blank=True, unique=False)
    email_professionnel=models.EmailField(null=True, blank=False)
    email_personnel=models.EmailField(null=True, blank=False)
    nometp=models.CharField(max_length=300, unique=False)
    fixe1=PhoneNumberField(blank=True)
    mobile1=PhoneNumberField(blank=True)
    email_personnel1=models.EmailField(null=True, blank=False)
    matricule=models.CharField(max_length=300, unique=False)
    Employeur=models.CharField(max_length=300, unique=False)
    D_affiliation=models.DateField(null=True, blank=False)
    D_engagement=models.DateField(null=True, blank=False)