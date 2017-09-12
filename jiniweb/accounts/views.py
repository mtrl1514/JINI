from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm 

from django.contrib.auth import models

# Create your views here.

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(settings.LOGIN_URL)
#     else:
#         form = UserCreationForm()
#     return render(request, 'app/about.html', {
#         'form': form,
#     }) 




def login(request):           
    if request.method == 'POST':
        form = auth.forms.AuthenticationForm(data=request.POST)
        if form.is_valid():    
            username = request.POST.get('username', 'guest')
            password = request.POST.get('password', 'guest')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)            
                if user.is_active:  
                    if user.is_superuser:
                        return HttpResponseRedirect('/admin')                     
                    else:
                        return HttpResponseRedirect('/admin')
                    
                    
                else:
                    # Return a 'disabled account' error message
                    return HttpResponseRedirect('/accounts/login') 
            else:
                # Return an 'invalid login' error message.
                return HttpResponseRedirect('/accounts/login')              
    else:            
        form = auth.forms.AuthenticationForm()
    return render(request, 'accounts/login.html', {
         'form': form,
    })

# def home(request):           
#     if request.method == 'POST':
#         form = auth.forms.AuthenticationForm(data=request.POST)
#         if form.is_valid():    
#             username = request.POST.get('username', 'guest')
#             password = request.POST.get('password', 'guest')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 auth.login(request, user)            
#                 if user.is_active:  
#                     if user.is_superuser:
#                         return HttpResponseRedirect('/admin')                     
#                     else:
#                         return HttpResponseRedirect('/admin')
                    
                    
#                 else:
#                     # Return a 'disabled account' error message
#                     return HttpResponseRedirect('/accounts/login') 
#             else:
#                 # Return an 'invalid login' error message.
#                 return HttpResponseRedirect('/accounts/login')              
#     else:            
#         form = auth.forms.AuthenticationForm()
#     return render(request, 'app/index.html', {
#          'form': form,
#     })