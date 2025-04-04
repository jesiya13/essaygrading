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
        fields = ['tname','tgender','age','tdepartment','tcontactno','tphoto','tcertificate','tqualification','treferenceletter','texp']
        widgets={
            'tname':forms.TextInput(attrs={'class':'form-control'}),
            'tgender':forms.Select(attrs={'class':'form-control'}),
            'tdepartment':forms.Select(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'tcontactno':forms.TextInput(attrs={'class':'form-control'}),
            'tphoto':forms.FileInput(attrs={'class':'form-control'}),
            'tcertificate':forms.FileInput(attrs={'class':'form-control'}),
            'tqualification':forms.TextInput(attrs={'class':'form-control'}), 
            'treferenceletter':forms.FileInput(attrs={'class':'form-control'}),
            'texp':forms.TextInput(attrs={'class':'form-control'}),

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
    department = forms.ChoiceField(label='Select Department')
    semester = forms.ChoiceField(label='Select Semester')

    def __init__(self, *args, **kwargs):
        super(attendance, self).__init__(*args, **kwargs)
        
        # Get the latest distinct departments and semesters from the database
        departments = Studentreg.objects.values_list('department', 'department').distinct()
        semesters = Studentreg.objects.values_list('semester', 'semester').distinct()

        # Dynamically set the choices
        self.fields['department'].choices = departments
        self.fields['semester'].choices = semesters

class attendanceview(forms.Form):
    date=forms.CharField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))


from django import forms
from .models import ElectiveCourse, SubjectView

class ElectiveForm(forms.ModelForm):
    elective_course = forms.ModelChoiceField(
        queryset=ElectiveCourse.objects.none(),  # Set dynamically in __init__
        empty_label="Select an elective",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = SubjectView
        fields = ['elective_course']

    def __init__(self, *args, **kwargs):
        student = kwargs.pop('student', None)  # Get logged-in student
        super().__init__(*args, **kwargs)

        if student:
            # Filter electives based on student's department & semester
            self.fields['elective_course'].queryset = ElectiveCourse.objects.filter(
                subject__dept=student.department,
                subject__sem=student.semester
            )


class uploadmark(forms.Form):
    department = forms.ChoiceField(label='Select Department')
    semester = forms.ChoiceField(label='Select Semester')

    def __init__(self, *args, **kwargs):
        super(uploadmark, self).__init__(*args, **kwargs)
        
        # Get the latest distinct departments and semesters from the database
        departments = Studentreg.objects.values_list('department', 'department').distinct()
        semesters = Studentreg.objects.values_list('semester', 'semester').distinct()

        # Dynamically set the choices
        self.fields['department'].choices = departments
        self.fields['semester'].choices = semesters

class internal(forms.ModelForm):
    class Meta:
        model=InternalMarks
        fields=['marks']
        widgets={
             'marks': forms.TextInput(attrs={'class': 'form-control'}),

         }  
        
class SubjectForm(forms.ModelForm):
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
        model = Subject
        fields = ['dept', 'sem']
        widgets = {
            'dept': forms.Select(attrs={'class': 'form-control mb-2'}),
            'sem': forms.Select(attrs={'class': 'form-control'}),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']

class ElectiveCourseForm(forms.ModelForm):
    class Meta:
        model = ElectiveCourse
        fields = ['name']

class InternalMarksForm(forms.ModelForm):
    class Meta:
        model = InternalMarks
        fields = ['marks']

class ComplaintForm(forms.ModelForm): 

    class Meta:
        model = complaints
        fields = ['complaint']
        widgets = {
            'complaint': forms.TextInput(attrs={'class': 'form-control'}),
              }
class ReplayForm(forms.ModelForm): 

    class Meta:
        model = complaints
        fields = ['replay']
        widgets = {
            'replay': forms.TextInput(attrs={'class': 'form-control'}),
              }
        
class Examdate(forms.ModelForm): 

    class Meta:
        model = exam
        fields = ['date','remark']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'remark': forms.TextInput(attrs={'class': 'form-control'}),
              }
class Essayup(forms.Form):
    essay = forms.FileField()