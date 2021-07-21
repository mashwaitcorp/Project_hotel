from django.shortcuts import render

# Create your views here.

def home_hotel(request, template_name="templates_hotel/index.html"):
    return render(request, template_name)