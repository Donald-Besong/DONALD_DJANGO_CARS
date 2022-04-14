from django.shortcuts import render
from .models import Team
from cars_app.models import Car

#from django.urls import reverse_lazy
#from django.views.generic.edit import CreateView

def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    data = {
      'teams': teams,
      'featured_cars': featured_cars,
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
