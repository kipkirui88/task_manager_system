from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Employees, Tasks


# Create your views here.

def dashboard(request):
    return render(request, 'employee/index.html')

# task views
@login_required
def Jobs(request):
    # Code for retrieving tasks assigned to the authenticated employee
    context = {"tasks": Tasks.objects.filter(employee=request.user)}
    return render(request, 'employee/task.html', context)

def edit_task(request, task_id):
    if request.method == 'POST':
        status = request.POST['status']
        task = Tasks.objects.get(id=task_id)
        task.status = status
        task.save()
        return redirect('Employee')
    


def Logout(request):
    return redirect('/')