from django.shortcuts import render
from django.views.generic import TemplateView
from portfolio import models

# Create your views here.

class IndexView(TemplateView):

    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Home
        home = models.Home.objects.latest('update_time')
        context['home'] = home

        #About
        about = models.About.objects.latest('updated')
        context['about'] = about

        # Experience
        experiences = models.Experience.objects.all()
        context['experiences'] = experiences


        #Skills
        categories = models.Category.objects.all()
        context['categories'] = categories

        #Projects
        projects = models.Project.objects.all()
        context['projects'] = projects

        return context




