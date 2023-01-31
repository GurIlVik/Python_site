from django.shortcuts import render
from django.http import HttpResponse

def index_pg1(request):
    return HttpResponse('описание сайта')
# Create your views here.
