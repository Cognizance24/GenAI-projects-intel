from django.shortcuts import render
import os
from app import get_courses_for_all_topics, topics
# from django.contrib.auth.decorators import login_required

def home(request):
    api_key = os.getenv('YOUTUBE_API_KEY')
    all_courses = get_courses_for_all_topics(api_key, topics)
    context = {'all_courses':all_courses}
    return render(request,'index.html',context)