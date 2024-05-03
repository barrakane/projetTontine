from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .forms import loginForm, SignUpForm


def login_view(request):

    form = loginForm(request.POST or None)
    if form.is_valid():    
        u = request.POST['username']
        p = request.POST['password']
      
        user = authenticate(username=u, password=p)       
        if user is not None:
            login(request, user)
            return redirect('/groupes')       
    return render(request, "utilisateur/login.html", {"form": form}) 



def register_user(request):
        if request.method == 'POST':
            form = SignUpForm(request.POST or None)
            if form.is_valid(): 
                form.save()
                u = request.POST['username']
                raw_password = request.POST['password1']
                user = authenticate(username=u, password=raw_password)
                return redirect("/login")
        else:
            form = SignUpForm()
            
        return render(request, "utilisateur/register.html", {"form": form})

