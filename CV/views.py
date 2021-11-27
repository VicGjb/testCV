from re import template
from django import forms
from django.db import models
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .forms import PersonForm, SkillForm
from .models import Person, Skill

class PersonDetailVeiew(DetailView):

    model = Person
    slug_field = 'url'

    # def get_context_data(self, **kwargs):
    #     context = super(self, Skill).get_context_data(**kwargs)
    #     return context

class SkillListVeiw(DetailView):

    model  = Skill
    queryset = Skill.objects.all()
    

class AddPersonView(View):

    def post(self,request):
        form = PersonForm(request.POST,  request.FILES)
        print(request.POST)
        print(request.POST['skill'])
        if form.is_valid:
            print('form.skill')
            form = form.save(commit=False)
            # skills_in_db = Skill.objects.all()
            # if form.skill not in skills_in_db:
            #     form.name = f'{form.skill}'
            #     form.save_m2m()
            # form.save()
            
        return redirect('http://127.0.0.1:8000/api/avigdor-brand-none')




class AddSkillView(View):
    def post(self, request,):
        form = SkillForm(request.POST)
        if form.is_valid:
            form = form.save(commit=False)
            skills_in_db = Skill.objects.all()
        return redirect('/')
        