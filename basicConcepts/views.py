from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Welc(request):
    return render(request,'index.html')


def User (request):
    name = request.GET['name']
    print (name)
    return render(request, 'user.html',{'name':name})