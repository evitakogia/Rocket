from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
import random
import json

def index(request):
    if request.method == "GET":
        points = [
                {"time": i,
                 "temp": 40*random.random(),
                 "press": 100*random.random(),
                 "alt": 10*random.random()} for i in range(20)]
        return JsonResponse(points, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        return HttpResponse("OK")
    else:
        return HttpResponseNotAllowed(["GET", "POST"])