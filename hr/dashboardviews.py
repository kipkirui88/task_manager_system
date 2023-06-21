from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Employees, Tasks, CustomUser


# Create your views here.

def dashboard(request):
    return render(request, 'dashboard/index.html')
# employees views
def Users(request):
    context = {"employees": Employees.objects.all(),
               "users": CustomUser.objects.all()}
    if request.method == 'POST':
        user = CustomUser.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        user.user_type = 3  # 3 corresponds to Employee
        user.save()

        employee = Employees(
            user=user,
            name=request.POST['name'],
            email=request.POST['email'],
            contact=request.POST['contact'],
            gender=request.POST['gender'],
            department=request.POST['department'],
            position=request.POST['position'],
            dor=request.POST['dor']
        )
        employee.save()
        messages.success(request, 'User Saved Successfully')
        return redirect('users')
    else: 
        messages.error(request, 'Invalid username or password. Please try again.')
        return render(request, 'dashboard/users.html', context)


# task views
def Jobs(request):
    context = {"tasks": Tasks.objects.all(),
               "users": CustomUser.objects.all()}
    
    if request.method == 'POST':
        employee = CustomUser.objects.get(username=request.POST.get('employee'))
        title = request.POST['title']
        description = request.POST['description']
        status = request.POST['status']
        start_date = request.POST['start_date']
        due_date = request.POST['due_date']

        add = Tasks(employee=employee, title=title, description=description, status=status, start_date=start_date, due_date=due_date)
        print('task added')
        add.save()
        return redirect('task')
    return render(request, 'dashboard/task.html', context)

def edit_task(request, task_id):
    if request.method == 'POST':
        status = request.POST['status']
        task = Tasks.objects.get(id=task_id)
        task.status = status
        task.save()
        return redirect('task')
    
def delete_task(request, task_id):
    task = Tasks.objects.get(id=task_id)
    task.delete()
    return redirect('task')
    
def Logout(request):
    return redirect('/')