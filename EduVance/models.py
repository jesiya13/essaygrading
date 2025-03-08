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


class teacherreg(models.Model):
    tphoto=models.FileField(upload_to='uploads/')
    tname=models.CharField(max_length=50)
    tgender=models.CharField(max_length=10)
    age=models.CharField(max_length=20)
    tdepartment=models.CharField(max_length=40)
    tcontactno=models.CharField(max_length=10)
    login_id=models.ForeignKey('Login', on_delete=models.CASCADE)
   
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

class Subjects(models.Model):
    dept=models.CharField(max_length=40)
    sem=models.CharField(max_length=40)
    course1=models.CharField(max_length=40)
    course2=models.CharField(max_length=40)
    course3=models.CharField(max_length=40)
    course4=models.CharField(max_length=40)
    ecourse1=models.CharField(max_length=40)
    ecourse2=models.CharField(max_length=40)
    ecourse3=models.CharField(max_length=40)
class SubjectView(models.Model):
    elective_course=models.CharField(max_length=40)
    current_date=models.DateTimeField(auto_now_add=True)
    stud_id=models.ForeignKey('studentreg', on_delete=models.CASCADE)



    