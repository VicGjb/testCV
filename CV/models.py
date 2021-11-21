from django.db import models
from django.db.models.aggregates import Max
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ManyToManyField


class Person(models.Model):
    """Person"""
    name = models.CharField(max_length=20, verbose_name='name')
    surname = models.CharField(max_length=30, verbose_name='name')
    photo = models.ImageField()
    about  = models.TextField(max_length=500, verbose_name='professional summary')

    class Meta:
        verbose_name='Person'
        verbose_name_plural='Persons'

class WorkHistory(models.Model):
    """Work experience"""
    worker = models.ForeignKey(Person, on_delete=CASCADE, primary_key=True, related_name='work_history')
    company = models.CharField(max_length=50, verbose_name='company name')
    position = models.CharField(max_length=20, verbose_name='position')
    date_start = models.DateField(verbose_name='start date')
    date_finish = models.DateField(verbose_name='finish date', null=True)
    description = models.TextField(verbose_name='about your work', null=True)

    class Meta:
        verbose_name='Work'
        verbose_name_plural='Works'

class Skill(models.Model):
    """Professional Skills"""
    person = ManyToManyField(Person)
    name = models.CharField(max_length=20, verbose_name='skill')

    class Meta:
        verbose_name='Skill'
        verbose_name_plural='Skills'

class Project(models.Model):
    """Portfolio projects"""
    person = models.ForeignKey(Person, on_delete=CASCADE, related_name='project')
    name = models.CharField(max_length=20, verbose_name='project name')
    link = models.CharField(max_length=50, null=True, verbose_name='link to project site')
    description = models.TextField(max_length=500, null=True, verbose_name='description of your project')

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'