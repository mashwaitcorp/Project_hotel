from django.shortcuts import render

# Create your views here.

def home_admin(request, template_name="templates_admin/index.html"):
    return render(request, template_name)
