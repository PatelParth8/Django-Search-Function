from django.shortcuts import render
from .models import *

# Create your views here.
def add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        query = Add(name=name, email=email, password=password)
        query.save()
    return render(request, 'add.html')

def display(request):
    fetch = Add.objects.all()
    return render(request, 'display.html', {'fetch': fetch})

def search(request):
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Add.objects.filter(name__contains = query_name)
            results = Add.objects.filter(email__contains = query_name)
            return render(request, 'search.html', {"results": results})
    return render(request, 'search.html')