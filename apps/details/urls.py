from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'details/(?P<job_id>\d+)$', views.jobdetails),
    url(r'postbid$', views.postbid),
    url(r'choosebid/(?P<job_id>\d+)/(?P<bid_id>\d+)$', views.choosebid),
]