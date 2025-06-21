# quiz/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('internet-quiz/', views.internet_quiz_view, name='internet_quiz'),
]
