from django.conf.urls import url
#from django.contrib.auth.views import login,logout
from accounts import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'
urlpatterns = [
    #url(r'^login/$', login,
    #    {'template_name': 'accounts/login.html'},
    #    name='login'),
    #url(r'^logout/$', logout,
    #    {'template_name': 'accounts/index.html'},
    #    name='logout')
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create_account, name='create_account'),
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name="login"),
    url(r'^logout/$', LogoutView.as_view(template_name='index.html'), name='logout'),
]
