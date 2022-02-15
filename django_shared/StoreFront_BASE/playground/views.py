from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say_hello(request):
    my_text = '<h1>Hello world</h1>'
    return HttpResponse(my_text)

def say_happy(request):
    my_name = 'Donald'
    my_age = 105
    args = {'name':my_name, 'age':my_age}
    return render(request, 'playground_home.html', args)
    
