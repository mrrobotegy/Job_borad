import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    titel = django_filters.CharFilter(lookup_expr='icontains')
    descraption = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['image','owner','Publishedon','experience','slug','Salary','Vacancy']