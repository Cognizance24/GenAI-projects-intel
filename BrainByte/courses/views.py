from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv

load_dotenv()

topics = {
     "python": "PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU",
    "data_science": "PLeo1K3hjS3us_ELKYSj_Fth2tIEkdKXvV",
    "web_development": "PLu0W_9lII9agq5TrH9XLIKQvv0iaF2X3w",
    "cyber_security":"PLhQjrBD2T383Cqo5I1oRrbC1EKRAKGKUE",
    "iot":"PL9ooVrP1hQOGccfBbP5tJWZ1hv5sIUWJl",
    "cloud_computing":"PL9ooVrP1hQOFtZ5oAAeOgi_nH-txMcDMu"
}

def get_playlist_items(playlist_id):
    """Fetches playlist items from the YouTube Data API."""
    api_key = os.getenv('YOUTUBE_API_KEY')
    url = "https://www.googleapis.com/youtube/v3/playlistItems"
    params = {
        "part": "snippet",
        "playlistId": playlist_id,
        "maxResults": 30,
        "key": api_key
    }
    response = requests.get(url, params=params)
    items = response.json().get('items', [])
    
    courses = []
    for item in items:
        course = {
            'name': item['snippet']['title'],
            'description': item['snippet']['description'],
            'image': item['snippet']['thumbnails']['high']['url'],
            'link': f"https://www.youtube.com/watch?v={item['snippet']['resourceId']['videoId']}"
        }
        courses.append(course)
    
    return courses

def courses(request):
    """View function to display a list of all courses/topics."""
    return render(request, 'courses/courses.html', {'topics': topics})

def show_topic(request, topic_name):
    """View function to display courses for a specific topic."""
    playlist_id = topics.get(topic_name)
    if playlist_id:
        courses = get_playlist_items(playlist_id)
        context = {
            'topic_name': topic_name,
            'courses': courses,
        }
        return render(request, 'courses/playlist.html', context)
    else:
        return render(request, 'courses/playlist.html', {'topic_name': topic_name})
