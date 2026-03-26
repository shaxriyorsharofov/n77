from django.shortcuts import render, redirect
from django.views import View
from .forms import *

# Create your views here.

class CategoryCreate(View):
    def get(self,request):
        form = CategoryForm()
        return render(request, 'category_create.html' , context={'form': form})
    
    
    def post(self, request):
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'category_create.html' , context={'form': form})

        
            


