from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Emp

# Create your views here.



def home(request):
    obj=Place.objects.all()
    obj1=Emp.objects.all()
    return render(request,'index.html',{'result':obj, 'res':obj1})


