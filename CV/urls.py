from django.urls import path
from .views import PersonDetailVeiew, AddPersonView, AddSkillView, SkillListVeiw

urlpatterns = [
    path('<slug:slug>', PersonDetailVeiew.as_view(), name='CV'),
    path('add_person/', AddPersonView.as_view(), name='add_person'),
    path('add_skill/', AddSkillView.as_view(), name='add_skill' ),
    
]