from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# @login_required
def login(request):
    return render(request,'users/login.html')

# @login_required
def logout(request):
    return render(request,'users/logout.html')

# @login_required
def signup(request):
    return render(request,'users/signup.html')