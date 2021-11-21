from django.urls import path
from .views import PersonDetailVeiew

urlpatterns = [
    path('<slug:slug>', PersonDetailVeiew.as_view(), name='CV'),

]