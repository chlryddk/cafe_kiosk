from django.shortcuts import get_object_or_404
from .models import *
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, View

def home(request):
    return render(request, 'base.html')

# class CategoryListView(ListView):
#     model = Category
#     template_name = 'base.html'
#     contenxt_object_name = 'object_list'
    
# class MenuDetailView(DetailView):
#     model = Menu
#     template_name = 'kiosk/kiosk_list.html'
#     context_object_name = 'object_list'

# class ProdectView(ListView):
#     model = Menu
#     template_name = 'menu_detail.html'
#     context_object_name = 

class ProductLV(ListView):
    model = Menu
    template_name = 'menu_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        if category_id:
            return Menu.objects.filter(category__id = category_id)
            # category = get_object_or_404(Category, id=category_id)
            # return category.menu_set.all()
        else:
            return Menu.objects.all()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['category'] = categories
        return context


    