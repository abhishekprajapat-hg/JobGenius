from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signUp, name="signup"),
    path('login/', views.logIn, name="login"),
    path('dashboard/', views.user_dashboard, name="dashboard"),
    path('logout/', views.user_logout, name="logout"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('jobs/', views.job_list, name="jobs"),
    path('publish/', views.publish_job, name="publish"),
    path('jobs/<int:job_id>/', views.job_details, name='job_details'),
    path('jobs/<int:job_id>/apply/', views.apply_job, name='apply_job'),
]
