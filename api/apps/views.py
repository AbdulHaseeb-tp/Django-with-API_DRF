from django.shortcuts import render
import requests

# Create your views here.

# def index(request):
#     response = requests.get('https://jsonplaceholder.typicode.com/users')
#     users = response.json()
#     return render(request, 'index.html', {'users': users})

def index(request):
    response = requests.get('https://fakestoreapi.com/products')
    items = response.json()
    return render(request, 'index.html', {'items': items})