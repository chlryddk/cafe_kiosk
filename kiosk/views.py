from .models import *
from django.shortcuts import render

from django.views.generic import ListView, DetailView

def home(request):
    return render(request, 'kiosk/home.html')

class CategoryListView(ListView):
    model = Category
    template_name = 'kiosk/category_list.html'
    contenxt_object_name = 'object_list'
    
class MenuDetailView(DetailView):
    model = Menu
    template_name = 'kiosk/kiosk_list.html'
    context_object_name = 'object_list'