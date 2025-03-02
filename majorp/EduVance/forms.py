from django import forms
from .models import *


class studentform(forms.ModelForm):
    gender_choices=(
        ('male','Male'),('female','Female'),('others','Others')
    )
    gender=forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect())
    # dob=forms.CharField(widget=forms.DateInput())
    class Meta:
        model = Studentreg
        fields = ['admno', 'name','address','gender','dob','department','semester','contactno']
        widget={
            'admno':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'department':forms.TextInput(attrs={'class':'form-control'}),
            'semester':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.TextInput(attrs={'type':'date'}),
            'contactno':forms.TextInput(attrs={'class':'form-control'}),
        } 
class loginform(forms.ModelForm):
    class Meta:
        model=Login
        fields=['email','password']

class login_check(forms.Form):
        email=forms.CharField(max_length=20)
        password=forms.CharField(max_length=10)