from django.db import models
JOB_TYPE = [
    ('Full time', 'Full time'),
    ('Part time', 'Part time'),
]

#upload image  
def upload_image(instance,filename):
    image_name , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)
    
# Create your models here.
#Job
class Job (models.Model):
    titel = models.CharField(max_length=25)
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    descraption = models.TextField(max_length=100)
    Publishedon = models.DateField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    Salary =models.IntegerField(default=0)
    experience =models.IntegerField(default=1) 
    category = models.ForeignKey('Catgory', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image)
    def __str__(self):
        return self.titel 
class Catgory(models.Model):
     name = models.CharField(max_length=25) 
     def __str__(self):
        return self.name
