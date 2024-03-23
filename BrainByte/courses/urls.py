from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses, name='courses'),
    path('topic/<str:topic_name>/', views.show_topic, name='show_topic'),
]
