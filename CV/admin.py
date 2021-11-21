from os import read
from ckeditor import widgets
from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.db.models import fields
from django.utils.safestring import mark_safe

from .models import Person, WorkHistory, Skill, Project, PersonSkill

admin.site.site_header = "CV"
admin.site.site_title = "CV"

"""**********************************FORMS**************************************"""
class PersonAdminForm(forms.ModelForm):
    """add CKeditor in person form"""
    about = forms.CharField(label='Professional summary', widget=CKEditorWidget())
    class Meta:
        model = Person
        fields = '__all__'


class WorkHistoryAdminForm(forms.ModelForm):
    """add CKeditor in WorkHistory form"""
    description = forms.CharField(label='About your work', widget=CKEditorWidget())

    class Meta:
        model = WorkHistory
        fields = '__all__'


class ProjectAdminForm(forms.ModelForm):
    """add CKeditor in Project form"""
    description = forms.CharField(label='About your work', widget=CKEditorWidget())

    class Meta:
        model = WorkHistory
        fields = '__all__'

"""**********************************InLines**************************************"""
class WorkHistoryInLine(admin.TabularInline):
    """Inline WorkHistory in PesonAdmin"""
    model = WorkHistory
    extra = 1
    fieldsets = (
        (None, {
            "fields": (
                (('worker', 'company', 'position', 'date_start', 'date_finish'),)
            ),
        }),
        (None, {
            "fields": (
                (('description',),)
            ),
        }),
    )

class ProjectInLine(admin.TabularInline):
    """Inline Projects in PesonAdmin"""
    model = Project
    extra = 1
    fields = ('name','link','description')
    
class SkilsInLine(admin.StackedInline):
    """Inline Skils in PesonAdmin"""
    model = PersonSkill
    extra = 3


"""**********************************Admins**************************************"""
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """Person"""
    list_display = ('id','name','surname', 'get_image')
    list_display_links = ('id','name','surname')
    search_fields = ('name','urname',)
    save_on_top=True
    form=PersonAdminForm
    inlines = [SkilsInLine, WorkHistoryInLine, ProjectInLine]
    readonly_fields = ('get_image',)
    fieldsets = (
        (None, {
            "fields": (
                (('name', 'surname','photo', 'get_image',),)
            ),
        }),
        (None, {
            "fields": (
                (('phone', 'email','city'),)
            ),
        }),
                (None, {
            "fields": (
                ('about',)
            ),
        }),
    )
    
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="110" height="110"')
    get_image.short_description='Photo'


@admin.register(WorkHistory)
class WorkHistoryAdmin(admin.ModelAdmin):
    """work History"""
    list_display = ('worker', 'company', 'position', 'date_start', 'date_finish')
    list_display_links = ('worker', 'company', 'position')
    search_fields = ('person',)
    save_on_top = True
    save_as = True
    form = WorkHistoryAdminForm
    fieldsets = (
        (None, {
            "fields": (
                (('worker'),)
            ),
        }),
        (None, {
            "fields": (
                (('company','position'),)
            ),
        }),     
        (None, {
            "fields": (
                (('date_start','date_finish'),)
            ),
        }),
        (None, {
            "fields": (
                (('description'),)
            ),
        }),   
    )
    

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Skills"""
    list_display = ('name',)
    list_display_links = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Projects"""
    list_display = ('person', 'name', 'link')
    list_display_links = ('person', 'name') 
    search_fields = ('person',)
    form = ProjectAdminForm
    fieldsets = (
        (None, {
            "fields": (
                (('person'),)
            ),
        }),
        (None, {
            "fields": (
                (('name', 'link'),)
            ),
        }),
                (None, {
            "fields": (
                (('description'),)
            ),
        }),
    )