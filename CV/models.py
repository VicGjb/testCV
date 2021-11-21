from django.core import validators
from django.db import models
from django.db.models.aggregates import Max
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ManyToManyField
from django.core.validators import RegexValidator
from django.utils.text import slugify

class Skill(models.Model):
    """Professional Skills"""
    name = models.CharField(max_length=20, verbose_name='skill')

    class Meta:
        verbose_name='Skill'
        verbose_name_plural='Skills'
    
    def __str__(self):
        return self.name

class Person(models.Model):
    """Person"""
    name = models.CharField(max_length=20, verbose_name='name')
    surname = models.CharField(max_length=30, verbose_name='surname')
    photo = models.ImageField('Avatar', upload_to="Person's photo", blank=True, null=True)
    about  = models.TextField(max_length=500, verbose_name='Professional summary', blank=True, null=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )
    phone = models.CharField(
        validators=[phone_regex], max_length=17, verbose_name='phone', blank=True, null=True
        )
    email = models.CharField(max_length=40, verbose_name='e-mail', blank=True, null = True)
    city =  models.CharField(max_length=100, verbose_name='address', blank=True, null = True)
    url = models.SlugField(max_length=160, unique=True, blank=True, null=True)
    skill = models.ManyToManyField(Skill, verbose_name='Skills', related_name='person_skill', blank=True, null=True)
    class Meta:
        verbose_name='Person'
        verbose_name_plural='Persons'

    def __str__(self):
        return f'{self.name} {self.surname}'

    def get_skills(self):
        return self.skills_set.all()


class WorkHistory(models.Model):
    """Work experience"""
    worker = models.ForeignKey(Person, on_delete=CASCADE, related_name='work_history')
    company = models.CharField(max_length=50, verbose_name='company name')
    position = models.CharField(max_length=20, verbose_name='position')
    date_start = models.DateField(verbose_name='start date')
    date_finish = models.DateField(verbose_name='finish date', blank=True, null=True)
    description = models.TextField(verbose_name='about your work',blank=True, null=True)

    class Meta:
        verbose_name='Work'
        verbose_name_plural='Works'

    def __str__(self):
        return f'{self.company} {self.position}'


class Project(models.Model):
    """Portfolio projects"""
    person = models.ForeignKey(Person, on_delete=CASCADE, related_name='project')
    name = models.CharField(max_length=20, verbose_name='project name')
    link = models.CharField(max_length=50, null=True, verbose_name='link to project site')
    description = models.TextField(
        max_length=500, null=True, verbose_name='description of your project'
        )

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return f"{self.person} project: {self.name}"
    

# class PersonSkill(models.Model): 
#     person = models.ForeignKey(Person, on_delete=CASCADE, related_name='skills')
#     skill = models.ForeignKey(Skill, on_delete=CASCADE)