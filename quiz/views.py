# quiz/views.py
from django.shortcuts import render, get_object_or_404, reverse
from .models import Quiz, QuizResponse, Answer, Section, Question
from .forms import build_quiz_form

def quiz_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    form = build_quiz_form(quiz)
    return render(request, 'quiz/quiz.html', {'quiz': quiz, 'form': form})

def internet_quiz_view(request):
    quiz = get_object_or_404(Quiz, title="Internet Quiz")
    QuizForm = build_quiz_form(quiz)
    if request.method == "POST":
        form = QuizForm(request.POST)
        if form.is_valid():
            response = QuizResponse.objects.create(quiz=quiz, uuid=request.POST.get('uuid', ''))
            for field_name, value in form.cleaned_data.items():
                if field_name.startswith('q_'):
                    qid = int(field_name.split('_')[1])
                    Answer.objects.create(response=response, question_id=qid, value=value)
            return render(request, "quiz/thanks.html", {"quiz": quiz})
    else:
        form = QuizForm()
    # Group questions by section for display
    sections = Section.objects.filter(quiz=quiz).order_by('name')
    section_questions = []
    for section in sections:
        qs = Question.objects.filter(section=section).order_by('order', 'id')
        section_questions.append((section, [form[f'q_{q.id}'] for q in qs]))
    return render(request, "quiz/internet_quiz.html", {
        "quiz": quiz,
        "form": form,
        "section_questions": section_questions,
    })


from django.shortcuts import render, redirect
from .forms import ProgrammerSurveyForm
from .models import ProgrammerResponse


def thanks_view(request):
    quiz = request.GET.get('quiz', 'Survey')
    return render(request, "quiz/thanks.html", {"quiz": quiz})

def programmer_survey_view(request):
    print("programmer_survey_view")
    submitted = False
    if request.method == 'POST':
        form = ProgrammerSurveyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data = form.cleaned_data
            data['languages'] = ', '.join(data['languages'])
            data['platforms'] = ', '.join(data['platforms'])
            data['favorite_areas'] = ', '.join(data['favorite_areas'])
            data['learning'] = ', '.join(data['learning'])
            ProgrammerResponse.objects.create(**data)
            submitted = True
            print("submitted")
            return redirect(f"{reverse('thanks')}?quiz=Programmer+Survey") 
    else:
        print("not submitted")
        form = ProgrammerSurveyForm()
    return render(request, 'quiz/programmer_survey.html', {
        'form': form,
        'submitted': submitted,
    })
