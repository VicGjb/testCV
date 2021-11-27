from django import forms
from django import forms
from django.forms import fields
from .models import Person, Skill

class PersonForm(forms.ModelForm):
    skill = forms.ModelMultipleChoiceField(queryset=Skill.objects.all())
    class Meta:
        model = Person
        fields = ('name','surname','photo',
        'phone','email','city','about','skill'
        )


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ('name',)