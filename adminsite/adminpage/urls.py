from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^rfid/$', views.timeInOut.as_view()),
    url(r'^$', views.index, name='index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)