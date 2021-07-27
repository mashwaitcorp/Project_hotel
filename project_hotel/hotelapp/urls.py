from django.urls import path
from .views.hotel_view import ArticleHome

urlpatterns = [
   
    path('', ArticleHome.as_view(), name="create"),
    
]