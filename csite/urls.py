from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns(
    "",
    url(r'^(?P<site_id>[0-9]+/$)', views.IndexView.as_view(), name='index'),
    url(r'^page/(?P<page_id>[0-9]+)/$', views.page_detail, name='page'),
)
