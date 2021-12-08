 # it look like Viwes in api
from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET']) 
def job_list_api(request):
    if request.method == 'GET':
        all_job =Job.objects.all()
        date = JobSerializer(all_job, many=True)
        return Response(date.data)
    
@api_view(['GET']) 
def job_details_api(request,id):
    if request.method == 'GET':
        job_details = Job.objects.get(id= id)
        date = JobSerializer(job_details)
        return Response(date.data)


class JobtList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobtDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field='id'