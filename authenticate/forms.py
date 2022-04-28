
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from authenticate. models import (User,)
from authenticate. models import (User,User_Info,State,Local_Government,\
Department,Country,)
import datetime
from django.contrib.auth.password_validation import validate_password
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User        
        fields = ['email']

class CustomUserCreationForm(forms.Form):
    id_numb = forms.CharField( widget=forms.TextInput(attrs={'class': 
    'form-control','placeholder': 'ID Number',}))
    id_numb.label=''
    id_numb.required
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password',}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password',}))
      
    def clean_id_numb(self):
        id_numb = self.cleaned_data['id_numb']        
        r = User.objects.filter(id_numb=id_numb)
        
        if r.count():
            raise  ValidationError("ID Number {} already exists".format(id_numb))
        return id_numb
 
 
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        user = self.cleaned_data.get('id_numb')
       
        validate_password(password1, user=user)
 
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
 
        return password2

   
    def save(self, commit=True):
        user = User.objects.create_user(
            # self.cleaned_data['email'],
            
            self.cleaned_data['id_numb'],
            self.cleaned_data['password1'],
            
        )
        return user


class AddNewUserForm(forms.ModelForm):
    staff_id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Staff ID',}))
    department=forms.ModelChoiceField(queryset=Department.objects.all(), label='Department',\
    widget=forms.Select(attrs={'class': 'form-control custom-select',}))

    rank=forms.ModelChoiceField(queryset=Country.objects.all(), label='Rank',\
    widget=forms.Select(attrs={'class': 'form-control custom-select',}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':\
    'First Name',}))
    
    
    middle_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':\
    'Middle Name',}))
    middle_name.required=False
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':\
    'Last Name',}))
    
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':\
    'Phone',}))
    region=forms.ModelChoiceField(queryset=Country.objects.all(), label='Region',\
    widget=forms.Select(attrs={'class': 'form-control custom-select',}))
   
    
    class Meta:
        model = User_Info
        fields = [ 'id_numb','department',]


