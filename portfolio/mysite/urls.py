from django.urls import path
from . import views

app_name = 'mysite'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('resume/', views.resume, name='resume'),
    path('about/', views.about, name='about'),
    path('matlab/', views.matlab, name='matlab'),
    path('web/', views.web, name='web'),
    path('proteus/', views.proteus, name='proteus'),
]