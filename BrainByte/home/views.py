from django.shortcuts import render
from app import get_courses_for_all_topics, topics
from pprint import pprint 
from django.http import HttpResponse
import openai, os
from django.shortcuts import render 
from django.http import JsonResponse 
from dotenv import load_dotenv
load_dotenv()
from .models import Chat
from django.utils import timezone

def home(request):
    topics = {
    "python": "PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU",
    "data_science": "PLeo1K3hjS3us_ELKYSj_Fth2tIEkdKXvV",
    "web_development": "PLu0W_9lII9agq5TrH9XLIKQvv0iaF2X3w",
    }
    api_key = os.getenv('YOUTUBE_API_KEY')
    all_courses = get_courses_for_all_topics(api_key, topics)
    # all_courses_list = list(all_courses.items()) # Python, Data Science, Web Dev
    context = {'all_courses': all_courses}

    # breakpoint()
    # pprint(all_courses.items)

    return render(request,'home/index.html',context)


OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

def get_completion(message): 
    print(message) 
    response = openai.ChatCompletion.create( 
        engine="text-davinci-003", 
        prompt=message, 
        max_tokens=1024, 
        n=1, 
        stop=None, 
        temperature=0.5, 
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ]
    ) 

    answer = response.choices[0].message.content.strip()
    print(answer)
    return answer


def query_view(request):
    chats = Chat.objects.filter(user=request.user)
    if request.method == 'POST': 
        message = request.POST.get('prompt') 
        response = get_completion(message)
        context = {'response':response}
        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now)
        chat.save()
        return JsonResponse({'message':message,'response': response}) 
    return render(request, 'home/chatbot_template.html', {'chats': chats})