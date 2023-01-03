from django import forms
from resourcebank. models import (Questions,Answers,Testsave,UploadFile)
from validators import (imagevalidator,pdfvalidator)



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

class AnswerForm(forms.ModelForm):
    answer = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':\
    '10','columns': '60',}))
    answer.required=True
    answer.label='Type your answer here:'
   

   

    class Meta:
        model = Answers
        fields = [ 'answer','file']


class TestsaveForm(forms.ModelForm):
    suggestion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':\
    '10','columns': '60',}))
    suggestion.required=True
    suggestion.label='Type your suggestion here:'
   

   

    class Meta:
        model = Testsave
        fields = [ 'suggestion','add_file']


class UploadFileForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':\
    '10','columns': '60',}))
    title.required=True
    title.label='Type your title and keywords here:'
    add_file = forms.FileField(validators=[pdfvalidator])

    class Meta:
        model = UploadFile
        fields = [ 'title','add_file']