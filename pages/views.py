from django.shortcuts import render

from django.views.generic import TemplateView

class homepageview(TemplateView):
    template_name = 'home.html'

class aboutpageiew(TemplateView):
    template_name = 'about.html'