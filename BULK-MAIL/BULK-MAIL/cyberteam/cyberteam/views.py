from django.http import HttpResponse
from django.shortcuts import render

def a(response):
    #return HttpResponse('a')
    return render(response, 'a.html')
def b(response):
    #return HttpResponse('b')
     return render(response,'b.html')
     