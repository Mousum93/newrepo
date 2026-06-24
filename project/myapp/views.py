from django.shortcuts import render,redirect
from myapp.models import *
from django.db.models import Q
import os
# Create your views here.

def index(request):
    persons = Person.objects.all()
    search = request.GET.get('search') 
    if search:
        persons = Person.objects.filter(
    Q(name__icontains=search) |
    Q(email__icontains=search)
)
    return render(request,"index.html",{"persons":persons}) 

def adduser(request):
    if request.method == 'POST':
        data = request.POST
        id = data.get ('id')
        name=data.get('name')
        age = data.get('age')
        email= data.get('email')
        image= request.FILES.get('image')
        if id:
            person = Person.objects.get(id=id)
            person.name=name
            person.age = age 
            person.email = email
            if image:
                if person.image:
                    os.remove(person.image.path)
                    person.image =image 
            person.save()
        else:
            Person.objects.create(name=name,age=age,email=email,image=image)


        

    return redirect('index') 

def delete(request):
    did = request.GET.get('did')
    po = Person.objects.get(id=did)
    os.remove(po.image.path)
    po.delete()
    return redirect('index') 

def update(request):
    uid=request.GET.get('uid')
    person=Person.objects.get(id=uid)
    persons = Person.objects.all()
    return render(request,"index.html",{"persons":persons,"person":person})