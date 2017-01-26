from django.forms.models import modelformset_factory
from django.shortcuts import render, get_object_or_404
from .models import Job
from django.views.generic import ListView
from .forms import AddJobForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class JobListView(ListView):
    queryset = Job.objects.filter(status='publicado')
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