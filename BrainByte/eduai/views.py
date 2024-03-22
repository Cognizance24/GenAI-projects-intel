from django.shortcuts import render
from .forms import QuestionnaireForm
from .models import Question

def edu_ai_questionnaire(request):
    if request.method == "POST":
        form = QuestionnaireForm(request.POST, questions=Question.objects.all())
        print([field.label for field in form])
        if form.is_valid():
            pass
    else:
        form = QuestionnaireForm(questions=Question.objects.all())
    return render(request, 'eduai/questionnaire.html', {'form': form})
