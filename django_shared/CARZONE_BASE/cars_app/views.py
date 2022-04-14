from django.shortcuts import render
from .models import Car

# Create your views here.
def cars(request):
    # teams = Team.objects.all()
    # data = {
      # 'teams': teams, 
     # }
    template_name = 'cars_templates/cars.html'
    return render(request, template_name)
    
def carservices(request):
    # teams = Team.objects.all()
    # data = {
      # 'teams': teams, 
     # }
    template_name = 'cars_templates/carservices.html'
    return render(request, template_name)
    
def search(request):
    cars = Car.objects.order_by('-created_date')
    data = {
      'cars': cars, 
     }
    template_name = 'cars_templates/search.html'
    return render(request, template_name, data)

