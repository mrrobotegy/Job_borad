
from django.urls.conf import path 
from . import views
from . import api

app_name ='job'

urlpatterns = [
    #Api list function base
    path('api/list',api.job_list_api,name='job_list_api'),
    path('api/jobs/<int:id>',api.job_details_api,name='job_details_api'),
    
    #Api list class base
    path('api/class/list',api.JobtList.as_view(),name='job_list_api'),
    path('api/class/jobs/<int:id>',api.JobtDetail.as_view(),name='job_details_api'),


 
    path('',views.job_list,name='job_list'),
    path('add',views.add_job,name='add_job'),
    path('<str:slug>',views.job_details,name='job_details'),
    
  
]