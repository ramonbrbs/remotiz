from django.forms.models import modelformset_factory
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Job
from django.views.generic import ListView
from .forms import AddJobForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.postgres.search import SearchVector

from rest_framework import generics
from jobs.serializers import JobSerializer

class JobListsAPI(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobListView(ListView):

    def get_queryset(self):
        search = self.request.GET.get('s')
        if search:
            return Job.objects.annotate(search=SearchVector('description', 'title')).filter(search=search).filter(status='publicado').order_by('-publish')


        return Job.objects.filter(status='publicado').order_by('-publish')
    #queryset = Job.objects.filter(status='publicado')
    context_object_name = 'jobs'
    paginate_by = 6
    template_name = 'list.html'

def details(request, slug):
    job = get_object_or_404(Job, slug=slug)
    return render(request,'detail.html', {'job': job,})

def addJob(request):
    if request.method == 'POST':
        jobForm = AddJobForm(data=request.POST)
        if jobForm.is_valid():
            newJob = jobForm.save()
    else:
        jobForm = AddJobForm()

    return render(request,'add.html',{'form': jobForm})