# quiz/models.py
from django.db import models

# Create your models here.

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

class Section(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='sections', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Question(models.Model):
    section = models.ForeignKey(Section, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=512)
    order = models.PositiveIntegerField(default=0)
    # Add more fields as needed (type, options, etc.)

class QuizResponse(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    uuid = models.CharField(max_length=64)

class Answer(models.Model):
    response = models.ForeignKey(QuizResponse, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    value = models.TextField()
