from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, TemplateView
# Create your views here.


class Recommender(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'recommender.html')
