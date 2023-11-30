from django.shortcuts import render,redirect
# from .models import Student
from .models import Contact
from django.contrib import messages
from django.utils import timezone
# Create your views here.
# def index(request):
#     data=Student.objects.all()
#     context={"data":data}
#     return render(request,"index.html",context)

# def about(request):
#     return render(request,"about.html")  



def index(request):
    data=Contact.objects.all()
    context={"data":data}
    return render(request,"list_page.html",context)

def create(request):
    return render(request,"create.html")

def insertData(request):
    
    if request.method=="POST":
        # data=Contact.objects.all()
        # for d in data:
        #     if d.name==name and d.email==email:
        #        messages.info(request,"Name already exists") 
        name=request.POST.get("name")
        email=request.POST.get("email")
        notes=request.POST.get("notes")
        time = timezone.now()
        print(name,email,notes,time)
        query=Contact(name=name,email=email,notes=notes,time=time)
        query.save()
        # data=Contact.objects.all()
        # context={"data":data}
        # messages.info(request,"Data inserted successfully")
        return render(request,"list_page.html")  
    
def updateData(request,id):
    
    if request.method=="POST":
        # id=request.POST.get("id")
        name=request.POST.get("name")
        email=request.POST.get("email")
        notes=request.POST.get("notes")
        editStudent = Contact.objects.get(id=id)
        editStudent.name=name
        editStudent.email=email
        editStudent.notes=notes
        # editStudent.time=time
        print("request ka",name,email,notes)
        print("NEw UPDATED OBJECT___________",editStudent.id,editStudent.name,editStudent.email,editStudent.notes,editStudent.time)
        editStudent.save()
        print("updated successfully")
        return redirect("/")
    else:
        print("Id------",id)
        data = Contact.objects.get(id=id)
        context={"data":data}
        print("else part ka context",data.id,data.name,data.email,data.notes,data.time)
        return render(request,"edit.html",context)
    
    

def deleteData(request,id):  
    if request.method=="POST":
       delContactObject= Contact.objects.get(id=id)
       delContactObject.delete()
       messages.info(request,"Data deleted successfully")
       return redirect("/")
    else:
        data=Contact.objects.get(id=id)
        deleteContext={"data":data}
        return render(request,"delete.html",deleteContext)