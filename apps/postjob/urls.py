from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^newjob$', views.postnewjob),
    url(r'^btaddjob$', views.BTaddjob),
    url(r'^newcategory$', views.addcategory),
    url(r'^btaddcategory$', views.BTaddcategory),
]