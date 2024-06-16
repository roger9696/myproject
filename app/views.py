from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world(request):
  name = request.GET.get('name', 'World')
  return HttpResponse(f'hello,{name}!')
