from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	url(r'^writerfid/$', views.writerfid.as_view()),
    url(r'^rfid/$', views.timeInOut.as_view()),
    url(r'^modules/$', views.modules.as_view()),    
    url(r'^studentlist/$', views.studentList.as_view()),    
    url(r'^profcheck/$', views.profCheck.as_view()),        
    url(r'^$', views.index.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)