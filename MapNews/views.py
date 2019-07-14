from django.shortcuts import render

def index(request):
    return render(request, 'main.html')

def get_values(request):
    return True