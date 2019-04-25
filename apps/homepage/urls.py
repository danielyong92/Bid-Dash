from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^onlinejob$', views.onlinejob),
    url(r'^automotive$', views.automotive),
    url(r'^house$', views.house),
    url(r'^pets$', views.pets),
    url(r'^photography$', views.photography),
    url(r'^misc$', views.misc),
]