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
class ElectiveCourseForm2(forms.ModelForm):
    class Meta:
        model = ElectiveCourse2
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

# 
class SubjectDetailForm(forms.ModelForm):
    major_1 = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Major 1'}))
    major_2 = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Major 2 (optional)'}))
    major_3 = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Major 3 (optional)'}))
    minors_1 = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Minor 1'}))
    minors_2 = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Minor 2'}))
    min_1 = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Minor 1'}))
    min_2 = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Minor 1'}))
    aec_1 = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AEC 1'}))
    aec_2 = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AEC 2'}))
    aecb_1 = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AECB 1'}))
    aecb_2 = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AECB 2'}))
    vac_1 = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'VAC 1'}))
    vac_2 = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'VAC 2'}))
    vac1 = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'VAC 1'}))
    vac2 = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'VAC 2'}))
    elective1 = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Elective 1'}))
    elective2 = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Elective 2'}))
    mdc1 = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MDC 1'}))
    mdc2 = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MDC 2'}))
    elective_1 = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Elective 1'}))
    elective_2 = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Elective 2'}))

    sec1 = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SEC1'}))
    sec2 = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SEC2'}))


    class Meta:
        
        model = SubjectDetail
        fields = ['mdc', 'sec', 'minorsone', 'minortwo','aeca', 'vac1','vac2', 'elective1','elective2' ,'aecb','major1','major2','major3']
    def clean(self):
        cleaned_data = super().clean()
        # Combine fields if they have values
        major1 = f"{cleaned_data.get('major_1')}".strip(", ")
        major2 = f"{cleaned_data.get('major_2')}".strip(", ")
        major3 = f"{cleaned_data.get('major_3')}".strip(", ")
        minors = f"{cleaned_data.get('minors_1')}, {cleaned_data.get('minors_2')}".strip(", ")
        minor2 = f"{cleaned_data.get('min_1')}, {cleaned_data.get('min_2')}".strip(", ")
        aeca = f"{cleaned_data.get('aec_1')}, {cleaned_data.get('aec_2')}".strip(", ")
        aecb = f"{cleaned_data.get('aecb_1')}, {cleaned_data.get('aecb_2')}".strip(", ")
        vac1 = f"{cleaned_data.get('vac_1')}, {cleaned_data.get('vac_2')}".strip(", ")
        vac2 = f"{cleaned_data.get('vac1')}, {cleaned_data.get('vac2')}".strip(", ")
        mdc = f"{cleaned_data.get('mdc1')}, {cleaned_data.get('mdc2')}".strip(", ")
        sec = f"{cleaned_data.get('sec1')}, {cleaned_data.get('sec2')}".strip(", ")
        electives = f"{cleaned_data.get('elective1')}, {cleaned_data.get('elective2')}".strip(", ")
        elective2 = f"{cleaned_data.get('elective_1')}, {cleaned_data.get('elective_2')}".strip(", ")

        # Assign values only if they are not empty
        cleaned_data['minorsone'] = minors if minors else None
        cleaned_data['minortwo'] = minor2 if minor2 else None
        cleaned_data['major1'] = major1 if major1 else None
        cleaned_data['major2'] = major2 if major2 else None
        cleaned_data['major3'] = major3 if major3 else None
        cleaned_data['mdc'] = mdc if mdc else None
        cleaned_data['sec'] = sec if sec else None
        cleaned_data['aeca'] = aeca if aeca else None
        cleaned_data['aecb'] = aecb if aecb else None
        cleaned_data['vac1'] = vac1 if vac1 else None
        cleaned_data['vac2'] = vac2 if vac2 else None
        cleaned_data['elective1'] = electives if electives else None
        cleaned_data['elective2'] = elective2 if elective2 else None


        return cleaned_data
# class StudentSelectionForm(forms.ModelForm):
#     class Meta:
#         unique_together = ('student',)  # ensures one selection per student
#         model = StudentSubjectSelection
#         fields = ['minorsone', 'minortwo', 'aeca', 'aecb', 'mdc', 'vac1', 'vac2', 'sec', 'elective1', 'elective2']

#     def __init__(self, *args, **kwargs):
#         detail = kwargs.pop('subject_detail', None)
#         super().__init__(*args, **kwargs)

#         if detail:
#             # Fields with multiple comma-separated options
#             selectable_fields = ['minorsone', 'minortwo', 'aeca', 'aecb','sec','vac1', 'vac2', 'elective1', 'elective2']
#             for field in selectable_fields:
#                 data = getattr(detail, field, '') or ''
#                 options = [opt.strip() for opt in data.split(',') if opt.strip()]
#                 self.fields[field].widget = forms.Select(
#                     choices=[('', '--- Select ---')] + [(opt, opt) for opt in options]
#                 )
#                 self.fields[field].required = False

#             # Fields with single values
#             if detail.mdc:
#                 self.fields['mdc'].widget = forms.Select(
#                     choices=[('', '--- Select ---'), (detail.mdc, detail.mdc)]
#                 )
#             else:
#                 self.fields['mdc'].widget = forms.Select(choices=[('', '--- No option available ---')])

class StudentSelectionForm(forms.ModelForm):
    class Meta:
        model = StudentSubjectSelection
        fields = ['minorsone', 'minortwo', 'aeca', 'aecb', 'mdc', 'vac1', 'vac2', 'sec', 'elective1', 'elective2']

    def __init__(self, *args, **kwargs):
        # Retrieve the subject details and student instance to adjust form dynamically
        detail = kwargs.pop('subject_detail', None)
        student = kwargs.pop('student', None)  # Get the student instance
        super().__init__(*args, **kwargs)

        if detail:
            semester = student.semester  # Access student's semester

            # Fields that could change based on semester
            selectable_fields = ['minorsone', 'minortwo', 'aeca', 'aecb', 'vac1', 'vac2', 'elective1', 'elective2','sec']

            # Clear all fields first to avoid showing irrelevant fields
            for field in selectable_fields + ['mdc', 'sec']:
                self.fields[field].widget = forms.HiddenInput()

            # Handle fields dynamically based on semester
            if semester == 1:
                self.fields['minorsone'].widget = forms.TextInput(attrs={'placeholder': 'Enter first minor subjects'})
                self.fields['minortwo'].widget = forms.TextInput(attrs={'placeholder': 'Enter second minor subjects'})
                self.fields['aeca'].widget = forms.TextInput(attrs={'placeholder': 'Enter AECA subjects'})
                self.fields['vac1'].widget = self.get_select_widget(detail.vac1)

            elif semester == 2:
                self.fields['minorsone'].widget = forms.TextInput(attrs={'placeholder': 'Enter first minor subjects'})
                self.fields['minortwo'].widget = forms.TextInput(attrs={'placeholder': 'Enter second minor subjects'})
                self.fields['aecb'].widget = forms.TextInput(attrs={'placeholder': 'Enter AECA subjects'})
                self.fields['elective1'].widget = self.get_select_widget(detail.elective1)

            elif semester == 3:
                self.fields['minorsone'].widget = self.get_select_widget(detail.minorsone)
                self.fields['minortwo'].widget = self.get_select_widget(detail.minortwo)
                self.fields['aeca'].widget = self.get_select_widget(detail.aeca)

            elif semester == 4:
                self.fields['mdc'].widget = self.get_select_widget(detail.mdc)
                self.fields['vac1'].widget = self.get_select_widget(detail.vac1)
                self.fields['vac2'].widget = self.get_select_widget(detail.vac2)

            elif semester == 5:
                self.fields['minorsone'].widget = self.get_select_widget(detail.minorsone)
                self.fields['minortwo'].widget = self.get_select_widget(detail.minortwo)
                self.fields['elective1'].widget = self.get_select_widget(detail.elective1)

            elif semester == 6:
                self.fields['minorsone'].widget = self.get_select_widget(detail.minorsone)
                self.fields['aeca'].widget = self.get_select_widget(detail.aeca)
                self.fields['vac2'].widget = self.get_select_widget(detail.vac2)

            elif semester == 7:
                self.fields['aecb'].widget = self.get_select_widget(detail.aecb)
                self.fields['elective1'].widget = self.get_select_widget(detail.elective1)

            elif semester == 8:
                self.fields['sec'].widget = self.get_select_widget(detail.sec)
                self.fields['mdc'].widget = self.get_select_widget(detail.mdc)

            # For all semesters, handle the common fields
            for field in selectable_fields:
                data = getattr(detail, field, '') or ''
                options = self.get_choices(data)
                self.fields[field].widget = forms.Select(
                    choices=[('', '--- Select ---')] + options
                )
                self.fields[field].required = False

            # Fields that have single values (e.g., mdc, sec)
            if detail.mdc:
                self.fields['mdc'].widget = forms.Select(
                    choices=[('', '--- Select ---'), (detail.mdc, detail.mdc)]
                )
            else:
                self.fields['mdc'].widget = forms.Select(choices=[('', '--- No option available ---')])

            if detail.sec:
                self.fields['sec'].widget = self.get_select_widget(detail.sec)
            else:
                self.fields['sec'].widget = forms.Select(choices=[('', '--- No option available ---')])

    def get_choices(self, data):
        """Helper method to safely split comma-separated values into choices."""
        if data:
            return [(opt.strip(), opt.strip()) for opt in data.split(',') if opt.strip()]
        return []

    def get_select_widget(self, field_data):
        """Helper method to generate a select widget."""
        choices = self.get_choices(field_data)
        return forms.Select(choices=[('', '--- Select ---')] + choices)
