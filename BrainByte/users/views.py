from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .form import RegisterUserForm

# register a customer
def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_user = True
            var.save()
            messages.info(request,'Your account has been created successfully! Please login to continue.')
            return redirect('login')
        else:
            messages.warning(request,'Something went wrong! Please check form inputs.')
            return redirect('register-user')
    else:
        form = RegisterUserForm()
        context = {'form': form}
        return render(request,'users/register_user.html',context)

# login a user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request,user)
            messages.info(request,'Logged in successfully! Please enjoy your session')
        else:
            messages.warning(request,'Something went wrong! Check your inputs')
            return redirect('login')
    else:
        return render(request, 'users/login.html')

# logout a user
def logout_user(request):
    logout(request)
    messages.info(request,'Logged out successfully! Please login to continue.')
    return redirect('login')