from decimal import Decimal
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Apartment

def api(request):
    longitude = float(request.GET['longitude'])
    latitude = float(request.GET['latitude'])
    apartments = Apartment.objects.filter(
            longitude__range = (longitude-0.01, longitude+0.01),
            latitude__range = (latitude-0.01, latitude+0.01),
            )
    if not apartments:
        return JsonResponse({'code':'empty'})
    names = [a.name for a in apartments]
    return JsonResponse({'code':'success','data':names})

def test(request):
    if request.method == 'GET':
        return render(request, 'apartment/test.html')
    else:
        name = request.POST['name']
        try:
            check = Apartment.objects.get(name=name)
            return HttpResponse('Had yet')
        except Apartment.DoesNotExist:
            apartment = Apartment(
                name = request.POST['name'],
                longitude = request.POST['longitude'],
                latitude = request.POST['latitude'],
            )
            apartment.save()
            return HttpResponse('success')
