from django.db import models    

class Studentreg(models.Model):
    photo=models.FileField(upload_to='uploads/')
    admno=models.CharField(max_length=10)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=40)
    gender=models.CharField(max_length=10)
    dob=models.DateField(max_length=20)
    department=models.CharField(max_length=40)
    semester=models.IntegerField()
    contactno=models.CharField(max_length=10)
    login_id=models.OneToOneField('Login', on_delete=models.CASCADE,related_name = 'student_as_loginid')

class Login(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=50)
    usertype=models.IntegerField(default=0,null=True)
    status=models.IntegerField(default=0)


class teacherreg(models.Model):
    tphoto=models.FileField(upload_to='uploads/')
    tname=models.CharField(max_length=50)
    tgender=models.CharField(max_length=10)
    age=models.CharField(max_length=20)
    tdepartment=models.CharField(max_length=40)
    tqualification=models.CharField(max_length=40)
    treferenceletter=models.FileField(upload_to='uploads/')
    tcertificate=models.FileField(upload_to='uploads/')
    texp=models.CharField(max_length=40)
    tcontactno=models.CharField(max_length=10)
    login_id=models.OneToOneField('Login', on_delete=models.CASCADE,related_name ='t')
   
class Essay(models.Model):
    essay=models.FileField(upload_to='uploads/')
    current_date=models.DateTimeField(auto_now_add=True)
    login_id=models.ForeignKey('Login', on_delete=models.CASCADE)
    tea_id=models.ForeignKey('teacherreg', on_delete=models.CASCADE)

    
class Answer(models.Model):
    answer=models.FileField(upload_to='uploads/')
    current_date=models.DateTimeField(auto_now_add=True)
    login_id=models.ForeignKey('Login', on_delete=models.CASCADE)
    t_id=models.ForeignKey('teacherreg', on_delete=models.CASCADE)

class Omr(models.Model):
    omr=models.FileField(upload_to='uploads/')
    current_date=models.DateTimeField(auto_now_add=True)
    login_id=models.ForeignKey('Login', on_delete=models.CASCADE)
    tc_id=models.ForeignKey('teacherreg', on_delete=models.CASCADE)
class Assignment(models.Model):
    assignment=models.FileField(upload_to='uploads/')
    current_date=models.DateTimeField(auto_now_add=True)
    login_id=models.ForeignKey('Studentreg', on_delete=models.CASCADE)
    ta_id=models.ForeignKey('teacherreg', on_delete=models.CASCADE)

class Attendance(models.Model):
    login_id=models.ForeignKey('Studentreg', on_delete=models.CASCADE)
    t_id=models.ForeignKey('teacherreg', on_delete=models.CASCADE)
    current_date=models.DateField(auto_now_add=True)
    present=models.IntegerField(default=0)
    absent=models.IntegerField(default=0)

class SubjectView(models.Model):
    stud_id = models.ForeignKey('Studentreg', on_delete=models.CASCADE)
    elective_course = models.CharField(max_length=40)
    semester = models.CharField(max_length=20)  # Store semester info
    current_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('stud_id', 'semester')  # Prevent multiple elective selections per semester

    def __str__(self):
        return f"{self.stud_id} - {self.elective_course} ({self.semester})"


class Subject(models.Model):
    dept = models.CharField(max_length=40)
    sem = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.dept} - {self.sem}"


class Course(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class ElectiveCourse(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='electives')
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class InternalMarks(models.Model):
    subject = models.ForeignKey('Course', on_delete=models.CASCADE)  # Connect marks to the subject
    marks = models.IntegerField(null=True, blank=True)  # Marks are now integers, allowing null/blank
    stud_id = models.ForeignKey('Studentreg', on_delete=models.CASCADE)  # Relating marks to student
    login_id = models.ForeignKey('teacherreg', on_delete=models.CASCADE)  # Teacher who entered the marks

    class Meta:
        unique_together = ('stud_id', 'subject')  # Prevent multiple marks entries for the same student-subject

    def __str__(self):
        return f"{self.stud_id} - {self.subject} - Marks: {self.marks}"

class complaints(models.Model):
     current_date = models.DateTimeField(auto_now_add=True)
     stud_id = models.ForeignKey('Studentreg', on_delete=models.CASCADE)
     complaint=models.CharField(max_length=100)
     replay=models.CharField(max_length=100)

class exam(models.Model):
     date = models.DateField(max_length=20)
     remark = models.CharField(max_length=60)
    