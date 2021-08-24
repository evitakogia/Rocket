import json
import datetime
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.utils import timezone
from . import models

def index(request):
    if request.method == "GET":
        points = models.Point.objects.filter(time_taken__time__gt=(timezone.now() - datetime.timedelta(seconds=60)))
        points = [
                {"time": str(p.time_taken.time()),
                 "temp": p.temperature,
                 "press": p.pressure,
                 "alt": p.altitute} for p in points]
        return JsonResponse(points, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        p = models.Point(time_taken=timezone.now(), pressure=data['Pressure']) # Need to finish...
        p.save()
        return HttpResponse("OK")
    else:
        return HttpResponseNotAllowed(["GET", "POST"])
