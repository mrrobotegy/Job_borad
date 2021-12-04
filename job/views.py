from typing import ContextManager
from django.shortcuts import render
from job.models import Job
from django.core.paginator import Paginator

# Create your views here.
def job_list(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list, 2) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'jobs' :page_obj} 
    return render(request,'job/job_list.html',context)

def job_details(request, id):
    job_details = Job.objects.get(id=id)
    context = {'job':job_details} 
    return render(request,'job/job_details.html',context)

 