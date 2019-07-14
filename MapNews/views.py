from django.shortcuts import render
from django.http import HttpResponse
from json import dumps

def index(request):
    return render(request, 'main.html', {'location': [{'lat': -13.1631, 'lng': -72.5450}, {'lat': 51.50072919999999, 'lng': -0.1246254},
                                                      {'lat': 53.5587, 'lng': 108.1650}, {'lat': 52.7229, 'lng': 23.6556}  ]} )

def get_values(request):
    if request.method == 'GET':
        s ={'location': [{'lat': -13.1631, 'lng': -72.5450}, {'lat': 51.50072919999999, 'lng': -0.1246254},
                                                      {'lat': 53.5587, 'lng': 108.1650}, {'lat': 52.7229, 'lng': 23.6556}  ]}
        return HttpResponse(dumps(s))
