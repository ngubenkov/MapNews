from django.shortcuts import render

def index(request):
    return render(request, 'main.html', {'f':{'lat': 51.50072919999999, 'lng': -0.1246254}})

def get_values(request):
    return True