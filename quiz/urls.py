# quiz/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('internet-quiz/', views.internet_quiz_view, name='internet_quiz'),
    path('programmer-experience/', views.programmer_survey_view, name='programmer_survey'),
    path('thanks/', views.thanks_view, name='thanks'),
]
