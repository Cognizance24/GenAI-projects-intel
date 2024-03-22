from django.urls import path
from . import views

urlpatterns = [
    path('questionnaire/', views.edu_ai_questionnaire, name='edu-ai-questionnaire'),
]