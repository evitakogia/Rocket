from django.http import JsonResponse
import random

def index(request):
    points = [
            {"time": i,
             "temp": 40*random.random(),
             "press": 100*random.random(),
             "alt": 10*random.random()} for i in range(20)]
    return JsonResponse(points, safe=False)
