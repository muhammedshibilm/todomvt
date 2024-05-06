from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Tododata


@login_required(login_url="login")
def home(request):
    if request.POST:
        data=request.POST.get('datas')
        status=Tododata.LIVE
        owner=request.user
        todo=Tododata.objects.create(owner=owner,status=status,tododata=data)
        todo.save()
        return redirect('dashboard')
    todos=Tododata.objects.filter(owner=request.user)
    return render(request,"dashboard.html",{'todos':todos,'data':None})

#When todo is compleded
@login_required(login_url="login")
def completed(request,id):
    status=Tododata.COMPLETE
    Tododata.objects.filter(id=id).update(status=status)
    return redirect('dashboard')

#When todo is deleted 
@login_required(login_url="login")
def deleted(request,id):
    Tododata.objects.filter(id=id).delete()
    return redirect('dashboard')

#When todo is edited 
@login_required(login_url="login")
def edited_mode(request, id):
    todo = Tododata.objects.get(id=id)
    return render(request, "edit_todo.html", {'todo': todo})

@login_required(login_url="login")
def update_todo(request, id):
    todo = Tododata.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST.get('datas')
        todo.tododata = data
        todo.save()
        return redirect('dashboard')
    return redirect('edit', id=id)


#User registeration
def singup(request):
    if request.POST:
        try:
           username=request.POST.get('username') 
           email=request.POST.get('email') 
           password=request.POST.get('password') 
           user =User.objects.create_user(username=username,email=email,password=password)
           user.save()
           return redirect('login')
        except Exception as e:
            error_message="Duplicate username or Invalid credential"
            print(error_message)
            return render(request,"singup.html", {"error":error_message})
    return render(request,"singup.html")

#User login session
def login(request):
    user=None
    error_message=None
    if request.POST:
        try:
           username=request.POST.get('username') 
           password=request.POST.get('password') 
           user =authenticate(username=username,password=password)
           if user:
               auth_login(request,user)
               return redirect('dashboard')
        except Exception as e:
            error_message="Invalid credential"
            return render(request,"login.html",{"error":error_message})
    return render(request,"login.html")

#user logout session
@login_required(login_url="login")
def logout(request):
    auth_logout(request)
    return redirect('login')