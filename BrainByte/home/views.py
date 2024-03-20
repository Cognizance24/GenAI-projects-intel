from django.shortcuts import render
import os
from app import get_courses_for_all_topics, topics
# from django.contrib.auth.decorators import login_required
from pprint import pprint 

def home(request):
    topics = {
    "python": "PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU",
    "data_science": "PLeo1K3hjS3us_ELKYSj_Fth2tIEkdKXvV",
    "web_development": "PLu0W_9lII9agq5TrH9XLIKQvv0iaF2X3w"
    }
    api_key = os.getenv('YOUTUBE_API_KEY')
    all_courses = get_courses_for_all_topics(api_key, topics)
    # all_courses_list = list(all_courses.items()) # Python, Data Science, Web Dev
    context = {'all_courses': all_courses}

    # breakpoint()
    # pprint(all_courses.items)

    return render(request,'home/index.html',context)