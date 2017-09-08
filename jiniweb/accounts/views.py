from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()
    return render(request, 'app/about.html', {
        'form': form,
    })   
 