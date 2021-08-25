import json
import datetime
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.utils import timezone
from . import models

def index(request):
    if request.method == "GET":
        points = models.Point.objects.filter(time_taken__time__gt=(timezone.now() - datetime.timedelta(seconds=60)))
        points = [
                {"time": i, #str(p.time_taken.time()),
                 "temp": float(p.temperature),
                 "press": float(p.pressure),
                 "alt": float(p.altitude)} for i,p in enumerate(points)]
        return JsonResponse(points, safe=False)
    elif request.method == "POST":
        body_unicode = request.body.decode('utf-8') 	
        data = json.loads(body_unicode) 	
        print(data)
        p = models.Point(time_taken=timezone.now(), temperature=data['temperature'], pressure=data['pressure'], altitude=data['altitude'])
        p.save()
        return HttpResponse("OK")
    else:
        return HttpResponseNotAllowed(["GET", "POST"])
