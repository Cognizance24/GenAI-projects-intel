from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register-user/', views.register_user, name='register-user'),
    path('profile/', views.show_profile, name='show_profile'),
]