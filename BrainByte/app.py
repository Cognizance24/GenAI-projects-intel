from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

topics = {
    "python": "PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU",
    "data_science": "PLeo1K3hjS3us_ELKYSj_Fth2tIEkdKXvV",
    "web_development": "PLu0W_9lII9agq5TrH9XLIKQvv0iaF2X3w",
    "cyber_security":"PLhQjrBD2T383Cqo5I1oRrbC1EKRAKGKUE",
    "iot":"PL9ooVrP1hQOGccfBbP5tJWZ1hv5sIUWJl",
    "cloud_computing":"PL9ooVrP1hQOFtZ5oAAeOgi_nH-txMcDMu",
    "app_development":"PLUhfM8afLE_Ok-0Lx2v9hfrmbxi3GgsX",
    "graphic_design":"PLW-zSkCnZ-gBA67ZtNUjIMfc_kwLo3MET",
    "video_editing":"PLW-zSkCnZ-gABGZU8--ISUauyewG40Yex"
}

def get_playlist_items(playlist_id, api_key):
    url = f"https://www.googleapis.com/youtube/v3/playlistItems"
    params = {
        "part": "snippet",
        "playlistId": playlist_id,
        "maxResults": 50,
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

@app.route('/')
def home():
    api_key = os.getenv('YOUTUBE_API_KEY')
    all_courses = get_courses_for_all_topics(api_key, topics)
    return render_template('index.html', all_courses=all_courses)

def get_courses_for_all_topics(api_key, topics):
    all_courses = {}
    for topic, playlist_id in topics.items():
        courses = get_playlist_items(playlist_id, api_key)
        all_courses[topic] = courses
    return all_courses

@app.route('/topic/<topic_name>')
def show_topic(topic_name):
    api_key = os.getenv('YOUTUBE_API_KEY')
    topic_formatted = topic_name.replace(" ", "_").lower() 
    playlist_id = topics.get(topic_formatted)
    if not playlist_id:
        return "Topic not found", 404
    courses = get_playlist_items(playlist_id, api_key)
    return render_template('playlist.html', courses=courses, topic_name=topic_name)

if __name__ == '__main__':
    app.run(debug=True)
