from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^login$', views.login),
    url(r'^signup$', views.signup),
    url(r'^register$', views.regacc),
    url(r'^loginbt$', views.logacc),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),
]