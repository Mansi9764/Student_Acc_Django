from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages
# Create your views here.
def index(request):
    data=Student.objects.all()
    context={"data":data}
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")  

def insertData(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        age=request.POST.get("age")
        gender=request.POST.get("gender")
        print(name,email,age,gender)
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save()
        messages.info(request,"Data inserted successfully")
        return render(request,"index.html")  

def updateData(request,id):
    
    if request.method=="POST":
        name=request.POST.get("name")   # or we can write as -> name=request.POST[name]
        email=request.POST.get("email")
        age=request.POST.get("age")
        gender=request.POST.get("gender")
        editStudent = Student.objects.get(id=id)
        editStudent.name=name
        editStudent.email=email
        editStudent.age=age
        editStudent.gender=gender
        editStudent.save()

        # query=Student(name=name,email=email,age=age,gender=gender)
        # query.save()
        return redirect("/")
   
    d=Student.objects.get(id=id)
    context={"d":d}
    return render(request,"edit.html",context)

def deleteData(request,id):
    if request.method=="POST":
       delStuObject= Student.objects.get(id=id)
       delStuObject.delete()
       messages.info(request,"Data deleted successfully")
       return redirect("/")
    else:
        deleteData=Student.objects.get(id=id)
        deleteContext={"deleteData": deleteData}
        return render(request,"delete.html",deleteContext)