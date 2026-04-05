from django.shortcuts import render, redirect
from django.views import View
from django.core.exceptions import ValidationError
from .forms import SignUpForm
# Create your views here.


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'auth/signup.html', {'form': form})
    
    def post(self, request):
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            raw_password = form.cleaned_data.get('password')
            user.set_password(raw_password)
            user.save()
            return redirect('index')
        return render(request, 'auth/signup.html', {'form': form})
        




