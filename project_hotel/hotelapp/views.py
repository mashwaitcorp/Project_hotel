from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models.hotel import Hotel, HotelCategory
from .forms.form import HotelForm, HotelCategoryForm

# Create your views here.


class HotelCreate(CreateView):
    
    model = Hotel
    form_class = HotelForm
    template_name="templates_hotel/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat_form = HotelCategoryForm()
        if cat_form.is_valid():
            new_cat = cat_form.save(commit=False)
            new_cat.save()

        context["cat_form"] = cat_form
        return context

    
    