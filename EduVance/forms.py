from django import forms
from .models import *

class studentform(forms.ModelForm):
    gender_choices = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    )
    gender = forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect())

    dept_choices = (
        ('bca', 'BCA'),
        ('bcom', 'B.Com.Computer Application'),
        ('bba', 'BBA'),
        ('b.a.english', 'B.A. English'),
        ('b.sc.psychology', 'B.Sc.Psychology'),
        ('b.com.taxation', 'B.Com.Taxation'),


    )
    department = forms.ChoiceField(choices=dept_choices, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Studentreg
        fields = ['admno', 'name', 'address', 'gender', 'dob', 'department', 'semester', 'contactno','photo']
        widgets = {
            'admno': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(),  # Radio buttons
            'department': forms.Select(attrs={'class': 'form-control'}),  # Select dropdown
            'semester': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'contactno': forms.TextInput(attrs={'class': 'form-control'}),
            'photo':forms.FileInput(attrs={'class':'form-control'}),

        }

class loginform(forms.ModelForm):
    class Meta:
        model=Login
        fields=['email','password']
        widgets={
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }

class login_check(forms.Form):
        email=forms.EmailField()
        password=forms.CharField(max_length=10)
        widgets={
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }
class teacherform(forms.ModelForm):
    gender_choices=(
        ('male','Male'),('female','Female'),('others','Others')
    )
    tgender=forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect())
    tdept_choices = (
        ('bca', 'BCA'),
        ('bcom', 'B.Com.Computer Application'),
        ('bba', 'BBA'),
        ('b.a.english', 'B.A. English'),
        ('b.sc.psychology', 'B.Sc.Psychology'),
        ('b.com.taxation', 'B.Com.Taxation'),
    )
    tdepartment = forms.ChoiceField(choices=tdept_choices, widget=forms.Select(attrs={'class': 'form-control'}))    
    class Meta:
        model = teacherreg
        fields = ['tname','tgender','age','tdepartment','tcontactno','tphoto']
        widgets={
            'tname':forms.TextInput(attrs={'class':'form-control'}),
            'tgender':forms.Select(attrs={'class':'form-control'}),
            'tdepartment':forms.Select(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'tcontactno':forms.TextInput(attrs={'class':'form-control'}),
            'tphoto':forms.FileInput(attrs={'class':'form-control'}),
        }         

class essayuploadform(forms.ModelForm):
    class Meta:
        model=Essay
        fields=['essay']
        # widgets={'essay':forms.FileField(attrs = {'class':'form-control'}),
        # }
class answersheet(forms.ModelForm):
    class Meta:
        model=Answer
        fields=['answer']

class omr(forms.ModelForm):
    class Meta:
        model=Omr
        fields=['omr']

class assignment(forms.ModelForm):
    class Meta:
        model=Assignment
        fields=['assignment']