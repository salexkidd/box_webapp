from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View
from django.http import HttpResponse
import simplejson

# Create your views here.

class TestTemplateView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("got it")


    def post(self, request, *args, **kwargs):
        print request.FILES
        print request.META
        return HttpResponse("HI")
