from django.shortcuts import render
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.forms import ModelForm, Textarea
from fiche_RP.models import information
from django import forms
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages




def accueil(request):
    #return HttpResponse("Hello world!")
    return render(request,'home.html')


def multistepformexample(request):

    return render(request,'multistepformexample.html')

def multistepformexample_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("multistepformexample"))
    else:
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        phone=request.POST.get("phone")
        twitter=request.POST.get("twitter")
        facebook=request.POST.get("facebook")
        gplus=request.POST.get("gplus")
        email=request.POST.get("email")
        password=request.POST.get("pass")
        cpass=request.POST.get("cpass")
        if password!=cpass:
            messages.error(request,"Confirm Password Doesn't Match")
            return HttpResponseRedirect(reverse('multistepformexample'))

        try:
            multistepform=MultiStepFormModel(fname=fname,lname=lname,phone=phone,twitter=twitter,facebook=facebook,gplus=gplus,email=email,password=password)
            multistepform.save()
            messages.success(request,"Data Save Successfully")
            return HttpResponseRedirect(reverse('multistepformexample'))
        except:
            messages.error(request,"Error in Saving Data")
            return HttpResponseRedirect(reverse('multistepformexample'))