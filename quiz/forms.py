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
