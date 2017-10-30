from django.conf.urls import url

from . import views

app_name='images'

urlpatterns = [
   #/images/
    url(r'^$', views.index, name='index'),
	#/images/id
    url(r'^(?P<id>[0-9]+)/$', views.image, name="image"),
    #/images/Nature
    url(r'nature/$', views.nature, name="nature"),
    #/images/People
    url(r'people/$', views.people, name="people"), 
    #/images/Urban
    url(r'urban/$', views.urban, name="urban"),
    #/images/Other
    url(r'other/$', views.other, name="other"),
]
