from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.


def index(request):
        return HttpResponse("Hello Word")

def homepage(request):
        return render(request, template_name= 'home.html', context={"name": "Azeez"})
