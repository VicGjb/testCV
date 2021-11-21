from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Person

class PersonDetailVeiew(DetailView):

    model = Person
    slug_field = 'url'

