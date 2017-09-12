from datetime import datetime
from django.conf.urls import url
from . import views
import django.contrib.auth.views
import app.forms


urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    # url(r'signup/$', views.signup, name='signup'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),    
    #url(r'logged_in/$', views.logged_in, name='logged_in'),
]