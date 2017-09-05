from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'login2/$', auth_views.login, name='login', kwargs={
        'template_name': 'app/login.html'
    }),
]