from django.shortcuts import render
# from django.contrib.auth import forms
from bookapp.forms import bookform
from bookapp.models import book
# Create your views here.

def home(request):
    return render(request,'home.html')
    
def upload(request):
    form=bookform()
    if(request.method=='POST'):
        form=bookform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request,'upload.html',{"form":form})
            

def show(request):
    k=book.objects.all()
    return render(request,'show.html',{"s":k})