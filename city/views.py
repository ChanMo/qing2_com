#!/usr/bin/python
# vim: set fileencoding=utf-8 :
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import City

@csrf_exempt
def api(request, city_id):
    try:
        if city_id != '0':
            city_list = City.objects.filter(parent_id=city_id)
        else:
            city_list = City.objects.filter(parent=None)
        json_list = []
        for city in city_list:
            json_list +=[{
                'id': city.id,
                'name': city.name,
            }]
        data = {'code':'ok','data':json_list}
    except (KeyError, City.DoesNotExist):
        data = {'code':'error'}
    return JsonResponse(data)


def test(request):
    return render(request, 'city/index.html')


def get_display(request, city_id):
    try:
        city = City.objects.get(id=city_id)
        data = {'code':'ok','data':city.tree_name(True)}
    except (KeyError, City.DoesNotExist):
        data = {'code':'error'}
    return JsonResponse(data)
