# quiz/forms.py
from django import forms
from .models import Quiz, Question

LIKERT_CHOICES = [
    ('0', 'N/A'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]

def build_quiz_form(quiz):
    class QuizForm(forms.Form):
        pass

    questions = Question.objects.filter(section__quiz=quiz).order_by('section__name', 'order', 'id')
    for q in questions:
        QuizForm.base_fields[f'q_{q.id}'] = forms.ChoiceField(
            label=q.text,
            choices=LIKERT_CHOICES,
            widget=forms.RadioSelect,
            required=True
        )
    return QuizForm

from django import forms

LANGUAGE_CHOICES = [
    ('Python', 'Python'),
    ('JavaScript', 'JavaScript'),
    ('Java', 'Java'),
    ('C/C++', 'C/C++'),
    ('Go', 'Go'),
    ('Rust', 'Rust'),
]
ALGORITHMS_CHOICES = [
    ('not_confidently', 'Not confidently'),
    ('with_help', 'With some help'),
    ('yes', 'Yes'),
]
DATA_STRUCTURES_CHOICES = [
    ('never', 'Never'),
    ('tutorials', 'Only in tutorials'),
    ('occasionally', 'Occasionally'),
    ('frequently', 'Frequently'),
]
CHALLENGES_CHOICES = [
    ('never', 'Never'),
    ('rarely', 'Rarely'),
    ('occasionally', 'Occasionally'),
    ('weekly', 'Yes, weekly'),
]
GIT_CHOICES = [
    ('never_used', 'Never used'),
    ('learning', 'Learning'),
    ('basic', 'Basic commands'),
    ('expert', 'Expert'),
]
CICD_CHOICES = [
    ('not_yet', 'Not yet'),
    ('team', 'Used in a team'),
    ('self', 'Set it up myself'),
]
TESTING_CHOICES = [
    ('rarely', 'Rarely test'),
    ('manual', 'Manual testing only'),
    ('integration', 'Integration tests'),
    ('unit', 'Unit tests'),
]
OPEN_SOURCE_CHOICES = [
    ('no', 'No'),
    ('interested', 'Interested'),
    ('yes', 'Yes'),
]
AGILE_CHOICES = [
    ('no', 'No'),
    ('somewhat', 'Somewhat familiar'),
    ('yes', 'Yes'),
]
ARCHITECTURE_CHOICES = [
    ('not_yet', 'Not yet'),
    ('personal', 'Yes, personal projects'),
    ('professional', 'Yes, professionally'),
]
CONCEPTS_CHOICES = [
    ('no', 'No'),
    ('basic', 'Basic familiarity'),
    ('strong', 'Strong understanding'),
]
DEPLOYMENT_CHOICES = [
    ('never', 'Never'),
    ('few', 'A few times'),
    ('frequently', 'Frequently'),
]
PLATFORMS_CHOICES = [
    ('github', 'GitHub Actions'),
    ('kubernetes', 'Kubernetes'),
    ('docker', 'Docker'),
    ('aws', 'AWS'),
]
FAVORITE_AREAS_CHOICES = [
    ("devops", "DevOps"),
    ("frontend", "Frontend"),
    ("games", "Games Development"),
    ("web", "Web Development"),
    ("backend", "Backend"),
    ("mobile", "Mobile"),
    ("desktop", "Desktop"),
    ("ai", "AI/ML"),
    ("data", "Data Science"),
    ("security", "Security"),
    ("other", "Other"),
]

class ProgrammerSurveyForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=64)
    last_name = forms.CharField(label="Last Name", max_length=64)
    age = forms.IntegerField(label="Age", min_value=0, max_value=150)
    years = forms.IntegerField(label="Years Programming", min_value=0, max_value=100)
    primary_language = forms.CharField(label="Primary Programming Language", max_length=64)
    languages = forms.MultipleChoiceField(
        label="Other Programming Languages",
        choices=LANGUAGE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    other_language = forms.CharField(label="Other Language (if not listed)", max_length=64, required=False)

    algorithms = forms.ChoiceField(
        label="Can you implement basic algorithms?",
        choices=ALGORITHMS_CHOICES,
        widget=forms.RadioSelect
    )
    data_structures = forms.ChoiceField(
        label="Used complex data structures?",
        choices=DATA_STRUCTURES_CHOICES,
        widget=forms.RadioSelect
    )
    challenges = forms.ChoiceField(
        label="Do you solve coding challenges?",
        choices=CHALLENGES_CHOICES,
        widget=forms.RadioSelect
    )
    git = forms.ChoiceField(
        label="Familiarity with Git",
        choices=GIT_CHOICES,
        widget=forms.RadioSelect
    )
    ci_cd = forms.ChoiceField(
        label="Worked with CI/CD pipelines?",
        choices=CICD_CHOICES,
        widget=forms.RadioSelect
    )
    testing = forms.ChoiceField(
        label="How do you test code?",
        choices=TESTING_CHOICES,
        widget=forms.RadioSelect
    )
    open_source = forms.ChoiceField(
        label="Open-source contributions?",
        choices=OPEN_SOURCE_CHOICES,
        widget=forms.RadioSelect
    )
    largest_project = forms.CharField(label="Largest project you've worked on", max_length=128)

    agile = forms.ChoiceField(
        label="Experience with Agile/Scrum?",
        choices=AGILE_CHOICES,
        widget=forms.RadioSelect
    )
    architecture = forms.ChoiceField(
        label="Designed a system architecture?",
        choices=ARCHITECTURE_CHOICES,
        widget=forms.RadioSelect
    )
    concepts = forms.ChoiceField(
        label="Familiarity with system design concepts?",
        choices=CONCEPTS_CHOICES,
        widget=forms.RadioSelect
    )
    deployment = forms.ChoiceField(
        label="Deployment experience?",
        choices=DEPLOYMENT_CHOICES,
        widget=forms.RadioSelect
    )
    platforms = forms.MultipleChoiceField(
        label="Platforms/tools used",
        choices=PLATFORMS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    platform_other = forms.CharField(label="Other Platform (if not listed)", max_length=64, required=False)
   
    favorite_areas = forms.MultipleChoiceField(
        label="Favorite Development Areas",
        choices=FAVORITE_AREAS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
   
    interests_other = forms.CharField(label="Other interests (if not listed)", max_length=128, required=False)
    learning = forms.MultipleChoiceField(
        label="How do you learn new technologies?",
        choices=[("rarely", "Rarely"), ("when_needed", "When needed"), ("every_few_months", "Every few months"), ("constantly", "Constantly")],
        widget=forms.RadioSelect,
        required=False
    )
    learning_other = forms.CharField(label="Other learning method (if not listed)", max_length=128, required=False)
