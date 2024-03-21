from django.shortcuts import render

def courses(request):
    render(request,'courses/playlist.html')

def show_topic(request, topic_name):
    context = {'topic_name': topic_name}
    return render(request, 'courses/show_topic.html', context)
