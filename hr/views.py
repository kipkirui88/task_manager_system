from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user_type = user.user_type
            if user_type == 1:  # Superuser
                return redirect('admin/')
            elif user_type == 2:  # HR
                return redirect('HR/')
            elif user_type == 3:  # Employee
                return redirect('Employee/')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
            
    return render(request, 'index.html')

def Logout(request):
    logout(request
    return redirect('/')

