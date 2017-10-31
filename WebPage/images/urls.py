from django.conf.urls import url

from . import views

app_name='images'

urlpatterns = [
   #/images/
    url(r'^$', views.index, name='index'),
    #/images/[lang]
    url(r'^(?P<lang>[A-Za-z]{2})/$', views.index, name='index'),
    #/images/[cat]
    url(r'^(?P<cat>[A-Za-z]{3,})/$', views.selection, name='selection'),
    #/images/[cat]/[lang]
    url(r'^(?P<cat>[A-Za-z]{3,})/(?P<lang>[A-Za-z]{2})$', views.selection, name='selection'),
]
