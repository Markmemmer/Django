from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class destination:
    place : str
    price : int
    desc  : str
    spec  : bool




def index(request):
    
    return render(request,'index.html')

def add(request):
    num1=int(request.POST['num1'])
    num2=int(request.POST['num2'])
    res=num1+num2
    return render(request,'add.html',{'result':res})