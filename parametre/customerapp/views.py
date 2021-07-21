from django.shortcuts import render

# Create your views here.

def home_customer(request, template_name="templates_customer/index.html"):
    return render(request, template_name)