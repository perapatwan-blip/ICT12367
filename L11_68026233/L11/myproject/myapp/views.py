from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Person  

def index(request):
    all_Person = Person.objects.all()
    return render(request, "index.html", {"all_person": all_Person})

# ✅ เพิ่มตัวนี้เข้าไป
def add_person(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        Person.objects.create(name=name, age=age)
        return redirect('/list')

    return render(request, "add.html")

def about(request):
    return render(request, "about.html")

def form(request):
    return render(request, "form.html")