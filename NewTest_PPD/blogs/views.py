from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request,'blogs/index.html')

def imageZip(request):
    return render(request,'blogs/imageZip.html')


