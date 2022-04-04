from django.shortcuts import render
#from django.urls import reverse_lazy
#from django.views.generic.edit import CreateView

def home(request):
    template_name = 'pages_templates/home.html'
    return render(request, template_name)

def about(request):
    template_name = 'pages_templates/about.html'
    return render(request, template_name)
    
def services(request):
    template_name = 'pages_templates/services.html'
    return render(request, template_name)
    
def contact(request):
    template_name = 'pages_templates/contact.html'
    return render(request, template_name)
