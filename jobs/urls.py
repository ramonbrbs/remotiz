from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt
app_name = 'job'
urlpatterns = [

    url(r'^$', csrf_exempt(views.JobListView.as_view()), name='jobs_list'),
    url(r'^jb/(?P<slug>[-\w]+)/$', views.details, name='job_detail'),
    url(r'^add/', views.addJob, name='job_add'),
]