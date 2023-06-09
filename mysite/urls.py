from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('projects/', views.ProjectList.as_view(), name='projects'),
    path('contact/', views.ContactPage.as_view(), name='contact')
]
