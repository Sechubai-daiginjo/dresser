from django.conf.urls import url, include
#from django.contrib.auth.views import login,logout
from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
#from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path(r'^create/$', views.create_account, name='create_account'),
    path(r'^login/$', LoginView.as_view(template_name='login.html'), name="login"),
    path(r'^logout/$', LogoutView.as_view(template_name='index.html'), name='logout'),
    path(r'^profile/$', views.Profile.as_view(), name='profile'),
    
]
