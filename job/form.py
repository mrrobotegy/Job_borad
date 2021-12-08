from django import forms
from django.db.models import fields
from .models import Apply, Job

class Apply_form(forms.ModelForm):
     class Meta:
        model = Apply
        fields = ['name','email','website','cv','cover_letter']

class AddJob (forms.ModelForm):
     class Meta:
        model = Job
        fields = "__all__"
        exclude = ("owner","slug")
         
         