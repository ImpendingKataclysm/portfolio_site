from django.shortcuts import render
from django.views import generic

from .models import Project


class HomePage(generic.TemplateView):
    template_name = 'index.html'


class AboutPage(generic.TemplateView):
    template_name = 'about.html'


class ProjectList(generic.ListView):
    queryset = Project.objects.get_queryset()
    template_name = 'projects.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
