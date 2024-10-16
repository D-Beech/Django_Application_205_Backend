#For testing, flask frontend app will take care of rendering webapages
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django_superchecker_project.scrape import *

def trees(request):
    return HttpResponse("Hello world and panda!")

def testing(request):
  template = loader.get_template('template.html')
  
  scrape_all()

  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))
