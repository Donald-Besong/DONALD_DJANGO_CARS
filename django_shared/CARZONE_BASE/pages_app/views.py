from django.shortcuts import render
from.models import Team
#from django.urls import reverse_lazy
#from django.views.generic.edit import CreateView

def home(request):
    teams = Team.objects.all()
    data = {
      'teams': teams, 
     }
    template_name = 'pages_templates/home.html'
    return render(request, template_name, data)

def about(request):
    teams = Team.objects.all()
    data = {
      'teams': teams, 
     }
    template_name = 'pages_templates/about.html'
    return render(request, template_name, data)
    
def services(request):
    template_name = 'pages_templates/services.html'
    return render(request, template_name)
    
def contact(request):
    template_name = 'pages_templates/contact.html'
    return render(request, template_name)
