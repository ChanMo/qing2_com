from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<city_id>[0-9]+)/$', views.api, name='index'),
    url(r'^get_display/(?P<city_id>[0-9]+)/$', views.get_display, name='get_display'),
    url(r'^test/$', views.test, name='test'),
]
