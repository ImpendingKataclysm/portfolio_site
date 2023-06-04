from django.shortcuts import render
from django.views import generic

from .models import Project
from .forms import ContactForm


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


class ContactPage(generic.FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '#'

    def form_valid(self, form):
        return super().form_valid(form)
