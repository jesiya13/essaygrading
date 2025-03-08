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
    sem_choices = (
        ('1', 'Semester 1'),
        ('2', 'Semester 2'),
        ('3', 'Semester 3'),
        ('4', 'Semester 4'),
        ('5', 'Semester 5'),
        ('6', 'Semester 6'),
        ('7', 'Semester 7'),
        ('8', 'Semester 8'),
    )
    semester = forms.ChoiceField(choices=sem_choices, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Studentreg
        fields = ['admno', 'name', 'address', 'gender', 'dob', 'department', 'semester', 'contactno','photo']
        widgets = {
            'admno': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(),  # Radio buttons
            'department': forms.Select(attrs={'class': 'form-control'}),  # Select dropdown
            'semester': forms.Select(attrs={'class': 'form-control'}),   # Select dropdown
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

class attendance(forms.Form):
    departments=Studentreg.objects.values_list('department','department').distinct()
    semesters=Studentreg.objects.values_list('semester','semester').distinct()
    department=forms.ChoiceField(choices=departments,label='Select department')
    semester=forms.ChoiceField(choices=semesters,label='Select semesters')

class attendanceview(forms.Form):
    date=forms.CharField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))

class subjects(forms.ModelForm):
    dept_choices = (
        ('choose department', 'Choose department'),
        ('bca', 'BCA'),
        ('bcom', 'B.Com.Computer Application'),
        ('bba', 'BBA'),
        ('b.a.english', 'B.A. English'),
        ('b.sc.psychology', 'B.Sc.Psychology'),
        ('b.com.taxation', 'B.Com.Taxation'),
    )
    dept = forms.ChoiceField(choices=dept_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    sem_choices = (
        ('choose semester', 'Choose semester'),
        ('1', 'Semester 1'),
        ('2', 'Semester 2'),
        ('3', 'Semester 3'),
        ('4', 'Semester 4'),
        ('5', 'Semester 5'),
        ('6', 'Semester 6'),
        ('7', 'Semester 7'),
        ('8', 'Semester 8'),
    )
    sem = forms.ChoiceField(choices=sem_choices, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Subjects
        fields = ['dept', 'sem', 'course1', 'course2', 'course3', 'course4', 'ecourse1', 'ecourse2','ecourse3']
        widgets = {
            'dept': forms.Select(attrs={'class': 'form-control'}),
            'sem': forms.Select(attrs={'class': 'form-control'}),
            'course1': forms.TextInput(attrs={'class': 'form-control'}),
            'course2': forms.TextInput(attrs={'class': 'form-control'}),
            'course3': forms.TextInput(attrs={'class': 'form-control'}),
            'course4': forms.TextInput(attrs={'class': 'form-control'}),
            'ecourse1': forms.TextInput(attrs={'class': 'form-control'}),
            'ecourse2': forms.TextInput(attrs={'class': 'form-control'}),
            'ecourse3':forms.TextInput(attrs={'class': 'form-control'}),
        }

class ElectiveForm(forms.Form):
    elective = forms.ChoiceField(choices=[])
    
    def set_elective_choices(self, elective_courses):
        # Dynamically set the choices for the elective dropdown
        choices = [(course, course) for course in elective_courses if course]
        self.fields['elective'].choices = choices