from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^dashboard$', views.dashboard),
    url(r'dashboard/cat/(?P<cat_id>\d+)$', views.dashboard_cat),
]