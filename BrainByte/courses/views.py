from django.shortcuts import render

def courses(request):
    render(request,'courses/playlist.html')