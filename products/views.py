from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse


class ProductList(ListView):
    model = Product
    ordering = ['position']

class ProductDetail(DetailView):
    model = Product

class ProductCreate(CreateView):
    model = Product
    fields = '__all__'


class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'


    
class ProductDelete(DeleteView): 
    model = Product

    def get_success_url(self):
        return reverse('product_list')
