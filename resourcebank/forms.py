from django import forms
from resourcebank. models import (Questions,Answers)
class QuestionsForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':\
    '7','columns': '3',}))
    description.required=True
    description.label='Type your questions here:'
    description.min_length=50
    
   
    
    class Meta:
        model = Questions
        fields = [ 'description']


class EditQuestionsForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':\
    '7','columns': '3',}))
    description.required=True
    description.label='Type your questions here:'
    # description.min_length=50
    
   
    
    class Meta:
        model = Questions
        fields = [ 'description']

# class AnswerForm(forms.ModelForm):
#     answer = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':\
#     '7','columns': '3',}))
#     answer.required=True
#     answer.label='Type your questions here:'
#     answer.min_length=50

#     class Meta:
#         model = Answers
#         fields = [ 'answer']
