from django.db import models    
import uuid

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
    teacherid = models.CharField(max_length=40, unique=True,editable=False)
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
    def save(self, *args, **kwargs):
        # Assign a shortened teacherid before saving, if it's not set
        if not self.teacherid:
            # Generate a UUID, and use the first 5 hexadecimal characters
            self.teacherid = uuid.uuid4().hex[:5]  # Get first 5 hex digits
        super(teacherreg, self).save(*args, **kwargs)
   
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
    subject = models.CharField(max_length=100)  # Connect marks to the subjec
    marks = models.IntegerField(null=True, blank=True)  # Marks are now integers, allowing null/blank
    stud_id = models.ForeignKey('Studentreg', on_delete=models.CASCADE)  # Relating marks to student
    login_id = models.ForeignKey('teacherreg', on_delete=models.CASCADE)  # Teacher who entered the marks

    def __str__(self):
        return f"{self.stud_id} - {self.subject} - {self.subjects}- Marks: {self.marks}"

class complaints(models.Model):
     current_date = models.DateTimeField(auto_now_add=True)
     stud_id = models.ForeignKey('Studentreg', on_delete=models.CASCADE)
     complaint=models.CharField(max_length=100)
     replay=models.CharField(max_length=100)

class exam(models.Model):
     date = models.DateField(max_length=20)
     remark = models.CharField(max_length=60)


class ElectiveCourse2(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='elective2')
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
class SubjectDetail(models.Model):
    major1 = models.TextField(null=True, blank=True)   # Example: "Math, Physics"
    major2 = models.TextField(null=True, blank=True)   # Example: "Math, Physics"
    major3= models.TextField(null=True, blank=True)   # Example: "Math, Physics"
    minorsone = models.TextField(null=True, blank=True)   # Example: "Math, Physics"
    minortwo = models.TextField(null=True, blank=True)   # Example: "Math, Physics"
    aeca = models.TextField(null=True, blank=True)      # Example: "Art, Music"
    aecb = models.TextField(null=True, blank=True)      # Example: "Art, Music"
    mdc = models.CharField(max_length=60, null=True, blank=True)
    vac1 = models.TextField(null=True, blank=True)      # Example: "Sports, Drama"
    vac2 = models.TextField(null=True, blank=True)      # Example: "Sports, Drama"
    sec = models.CharField(max_length=60, null=True, blank=True)
    elective1 = models.TextField(null=True, blank=True)  # Example: "Art, Music"
    elective2= models.TextField(null=True, blank=True)  # Example: "Art, Music"


    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='details')

    def __str__(self):
        return f"Details for {self.subject.dept} - {self.subject.sem}"
    
class StudentSubjectSelection(models.Model):
    student = models.ForeignKey('Studentreg', on_delete=models.CASCADE)
    subject = models.ForeignKey('SubjectDetail', on_delete=models.CASCADE,null=True)

    minorsone = models.CharField(max_length=100, null=True, blank=True)
    minortwo = models.CharField(max_length=100, null=True, blank=True)
    aeca = models.CharField(max_length=100, null=True, blank=True)
    aecb = models.CharField(max_length=100, null=True, blank=True)
    mdc = models.CharField(max_length=100, null=True, blank=True)
    vac1 = models.CharField(max_length=100, null=True, blank=True)
    vac2 = models.CharField(max_length=100, null=True, blank=True)
    sec = models.CharField(max_length=100, null=True, blank=True)
    elective1 = models.CharField(max_length=100, null=True, blank=True)
    elective2 = models.CharField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.subject.dept} Sem {self.subject.sem} Selection"
