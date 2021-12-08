from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.text import slugify
from django.contrib.auth.models import User
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
    owner = models.ForeignKey(User, related_name='add_job', on_delete=models.CASCADE)
    titel = models.CharField(max_length=25)
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    descraption = models.TextField(max_length=100)
    Publishedon = models.DateField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    Salary =models.IntegerField(default=0)
    experience =models  .IntegerField(default=1) 
    category = models.ForeignKey('Catgory', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image)
    
    slug = models.SlugField()
    def save(self,*args, **kwargs):
        self.slug =slugify(self.titel)
        super(Job,self).save(*args, **kwargs)
        
    def __str__(self):
        return self.titel 
class Catgory(models.Model):
     name = models.CharField(max_length=25) 
     def __str__(self):
        return self.name

class Apply(models.Model):
    job = models.ForeignKey(Job ,related_name='apply_job', on_delete=CASCADE)
    name = models.CharField(max_length=50)
    email =models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    published_at = models.DateField(auto_now=True)
    def __str__(self) :
        return self.name