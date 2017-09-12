"""
Definition of urls for jiniweb.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from datetime import datetime
from django.conf.urls import include, url
import django.contrib.auth.views

import app.forms
import app.views
import accounts.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    
    #url(r'^contact$', app.views.contact, name='contact'),
    #url(r'^about', app.views.about, name='about'),
    # url(r'^login/$',
    #     django.contrib.auth.views.login,
    #     {
    #         'template_name': 'app/login.html',
    #         'authentication_form': app.forms.BootstrapAuthenticationForm,
    #         'extra_context':
    #         {
    #             'title': 'Log in',
    #             'year': datetime.now().year,
    #         }
    #     },
    #     name='login'),
    # url(r'^logout$',
    #     django.contrib.auth.views.logout,
    #     {
    #         'next_page': '/',
    #     },
    #     name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^app/', include('app.urls')),
    url(r'^$', app.views.home, name='home'),
    #url(r'^$',accounts.views.home, name='home'),
    url(r'^accounts/', include('accounts.urls')),
]
