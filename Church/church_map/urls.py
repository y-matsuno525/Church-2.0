from django.urls import path,include
from . import views

app_name = "church_map"

urlpatterns = [
    path('',views.church_map,name='map'),
]
