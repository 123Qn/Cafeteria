from django.http import HttpResponse
from django.template import loader

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())
def desert(request):
  template = loader.get_template('dessert.html')
  return HttpResponse(template.render())
def drink(request):
  template = loader.get_template('drink.html')
  return HttpResponse(template.render())
def dining(request):
  template = loader.get_template('dining.html')
  return HttpResponse(template.render())
