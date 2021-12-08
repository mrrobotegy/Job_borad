from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from accounts.form import Signupform ,ProfileForm,UserForm
from .models import Profile
from django.urls import reverse
# Create your views here.

def signup(request):
    if request.method=="POST":
        form =Signupform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
            
    else:
        form= Signupform()
    return render(request,'registration/signup.html',{"form":form})


def profile(request):
     profile = Profile.objects.get(user=request.user )
     return render(request,'accounts/profile.html',{"profile":profile})



def profile_edit (request):
     #get the user first 
    profile = Profile.objects.get(user=request.user )
    if request.method=='POST':
        ueserform =UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile)
        if ueserform.is_valid() and profileform.is_valid():
            ueserform.save()
            myprofile=profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))
            
    else:
        ueserform =UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
        
    return render(request,'accounts/profile_edit.html',{'profileform':profileform,'userform':ueserform})
    
   
   