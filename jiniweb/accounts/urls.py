from datetime import datetime
from django.conf.urls import url
from . import views
import django.contrib.auth.views
import app.forms


urlpatterns = [
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'accounts/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log In',
                'year': datetime.now().year,
            }            
        },
        name='login'),
    # url(r'signup/$', views.signup, name='signup'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
]