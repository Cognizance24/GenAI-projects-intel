from django.shortcuts import render
from django.http import JsonResponse
import json

def recommend_courses(preferences):
    print("User Preferences:", preferences)
    """
    Generate course recommendations based on user preferences.
    """
    all_courses = [
        {"name": "Intro to Programming", "topic": "programming", "method": "visual", "hours_required": 5},
    {"name": "Data Science Fundamentals", "topic": "data science", "method": "textual", "hours_required": 8},
    {"name": "Ethical Hacking for Beginners", "topic": "cybersecurity", "method": "video", "hours_required": 10},
    {"name": "Cloud Computing with AWS", "topic": "cloud computing", "method": "video", "hours_required": 6},
    {"name": "Blockchain Basics", "topic": "blockchain", "method": "textual", "hours_required": 4},
    {"name": "AI for Everyone", "topic": "artificial intelligence", "method": "interactive", "hours_required": 7},
    {"name": "Introduction to IoT", "topic": "internet of things", "method": "interactive", "hours_required": 5},
    {"name": "Machine Learning with Python", "topic": "data science", "method": "project-based", "hours_required": 12},
    {"name": "Web Development from Scratch", "topic": "web development", "method": "video", "hours_required": 15},
    {"name": "Advanced Java Programming", "topic": "programming", "method": "project-based", "hours_required": 10},
    {"name": "Creative Writing", "topic": "arts and humanities", "method": "textual", "hours_required": 3},
    {"name": "Entrepreneurship 101", "topic": "business and economics", "method": "interactive", "hours_required": 5},
    {"name": "Digital Marketing Strategies", "topic": "business and economics", "method": "video", "hours_required": 4},
    {"name": "Basic Electronics", "topic": "science and technology", "method": "project-based", "hours_required": 8},
    {"name": "Photography for Beginners", "topic": "arts and humanities", "method": "visual", "hours_required": 6},
    {"name": "Python for Data Analysis", "topic": "data science", "method": "interactive", "hours_required": 10},
    ]

    recommended_courses = [
        course["name"] for course in all_courses
        if course["topic"] in preferences["topics_of_interest"]
        and course["method"] == preferences["learning_method"]
        and course["hours_required"] <= preferences["time_availability"]
    ]
    for course in all_courses:
        print("Checking course:", course["name"])
        if course["topic"] in preferences["topics_of_interest"]:
            if course["method"] == preferences["learning_method"]:
                if course["hours_required"] <= preferences["time_availability"]:
                    recommended_courses.append(course["name"])
                    print("Course matched:", course["name"])
    
    return recommended_courses


def edu_ai_questionnaire(request):
    return render(request, 'eduai/questionnaire.html')

def questionnaire_submission(request):
    """
    Handle questionnaire submissions and return recommendations.
    """
    if request.method == "POST":
        data = json.loads(request.body)
        
        preferences = {
            "learning_method": data.get("learning_method"),
            "topics_of_interest": data.get("topics_of_interest", []),
            "time_availability": int(data.get("time_availability", 0)),
        }
        
        recommendations = recommend_courses(preferences)
        
        return JsonResponse({"recommendations": recommendations})
    else:
        return JsonResponse({"error": "This method only supports POST requests."}, status=405)

def submit_questionnaire(request):
    if request.method == "POST":
        return render(request, "eduai/recommendations.html")
    else:
        return render(request, "eduai/questionnaire.html")