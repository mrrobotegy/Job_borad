from django.contrib import admin

from job.models import Apply, Job , Catgory

# Register your models here.
admin.site.register(Job) 
admin.site.register(Apply)
admin.site.register(Catgory)