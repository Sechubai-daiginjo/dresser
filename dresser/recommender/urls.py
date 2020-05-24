from django.conf.urls import include, url
from . import views
from django.urls import path

app_name = 'recommender'

urlpatterns = [
    path('recommender/', views.Recommender.as_view(), name='recommender'),
]
