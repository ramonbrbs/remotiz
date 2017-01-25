from django.shortcuts import render, get_object_or_404
from .models import Job
from django.views.generic import ListView

class JobListView(ListView):
    queryset = Job.objects.all()
    context_object_name = 'jobs'
    paginate_by = 8
    template_name = 'list.html'

def details(request, slug):
    job = get_object_or_404(Job, slug=slug)
    return render(request,'detail.html', {'job': job,})