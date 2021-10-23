from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from myapp.forms import MyForm
from myapp import models

def index(request):
    return render(request,'myapp/index.html')

def about(request):
    return render(request,'myapp/about.html')

def resume(request):
    return render(request,'myapp/resume.html')

def skills(request):
    return render(request,'myapp/skills.html')

def projects(request):
    return render(request,'myapp/projects.html')

def feedback(request):
    if request.method=="POST":
        form = MyForm(request.POST)

        if form.is_valid():
            fname = request.POST['firstname']
            lname = request.POST['lastname']
            email = request.POST['email']
            comments = request.POST['comments']
            rate = request.POST['rating']

            ins = models.Resume(firstname=fname,lastname=lname,email=email,rating=rate,comments=comments)
            ins.save()

            return thankyou(request)
    else:
        form = MyForm()
        return render(request,'myapp/feedback.html',{'form':form})

def thankyou(request):
    return render(request,'myapp/thankyou.html')
