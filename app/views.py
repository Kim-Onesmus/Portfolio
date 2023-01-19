from django.shortcuts import render
from .models import Project, Product

# Create your views here.

def Home(request):
    project = Project.objects.all()
    context = {'project':project}
    return render(request, 'app/homepage.html', context)

def KimTech(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'app/kimtech.html', context)

def Messanges(request):
    return render(request, 'app/messange.html')