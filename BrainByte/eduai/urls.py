from django.urls import path
from . import views

urlpatterns = [
    path('questionnaire/', views.edu_ai_questionnaire, name='edu-ai-questionnaire'),
    # path('submit_questionnaire', views.questionnaire_submission, name='submit-questionnaire'),
    path('submit_questionnaire', views.submit_questionnaire, name='submit_questionnaire'),
]