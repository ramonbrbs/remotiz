from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.JobListView.as_view(), name='jobs_list'),
    url(r'^jb/(?P<slug>[-\w]+)/$', views.details, name='job_detail'),
]