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

class ProgrammerResponse(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveIntegerField()
    years = models.PositiveIntegerField()
    primary_language = models.CharField(max_length=64)
    languages = models.CharField(max_length=256)
    other_language = models.CharField(max_length=64, blank=True)
    algorithms = models.CharField(max_length=64)
    data_structures = models.CharField(max_length=64)
    challenges = models.CharField(max_length=256)
    git = models.CharField(max_length=64)
    ci_cd = models.CharField(max_length=64)
    testing = models.CharField(max_length=64)
    open_source = models.CharField(max_length=64)
    largest_project = models.CharField(max_length=128)
    agile = models.CharField(max_length=64)
    architecture = models.CharField(max_length=64)
    concepts = models.CharField(max_length=128)
    deployment = models.CharField(max_length=128)
    platforms = models.CharField(max_length=128)
    platform_other = models.CharField(max_length=64, blank=True)
    favorite_areas = models.CharField(max_length=128, blank=True)
    interests_other = models.CharField(max_length=128, blank=True)
    learning = models.TextField()
    learning_other = models.CharField(max_length=128, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.age})"
