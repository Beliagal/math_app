from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm

class RegisterView (View):
    def get (self, request):
        form = UserCreationForm()
        return render (request, 'register.html', {'form': form})
        
    def post (self, request):
        pass