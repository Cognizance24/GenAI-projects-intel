# eduai/forms.py
from django import forms
from .models import UserResponse, Question

class QuestionnaireForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions', Question.objects.all())  # Provide a default query
        super(QuestionnaireForm, self).__init__(*args, **kwargs)
        
        for question in questions:
            if question.question_type == 'text':
                self.fields[f'question_{question.id}'] = forms.CharField(label=question.text)
            elif question.question_type == 'choice':
                choices = [(choice.id, choice.text) for choice in question.choices.all()]
                self.fields[f'question_{question.id}'] = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
