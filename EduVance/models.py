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
    login_id=models.ForeignKey('Login', on_delete=models.CASCADE)

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



    