from django.shortcuts import render
#from django.urls import reverse_lazy
#from django.views.generic.edit import CreateView

#class home(CreateView):
#    success_url = reverse_lazy('home')
#    template_name = 'pages_templates/home.html'

def home(request):
    template_name = 'pages_templates/home.html'
    return render(request, template_name)
