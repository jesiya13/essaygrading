from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages
from django.db.models import Q

def main(request):
    return render(request, 'main.html')
def admin(request):
    return render(request, 'admin.html')
def user(request):
    return render(request, 'user.html')
def tuser(request):
    return render(request, 'tuser.html')
def studentreg(request):
    if request.method == 'POST':
        form=studentform(request.POST,request.FILES)
        logins=loginform(request.POST)
        print(form)
        if form.is_valid() and logins.is_valid():
            a=logins.save(commit=False)
            a.usertype=1
            a.save()
            b=form.save(commit=False)
            b.login_id=a
            b.save()
            messages.success(request,"Form successfully submitted")
        return redirect('main')
    else:
        form=studentform()
        logins=loginform()
    return render(request,'studentreg.html',{'form':form,'login':logins})
def adminstudview(request):
    view_id=Studentreg.objects.all()
    return render(request,'adminstudview.html',{'data':view_id})

def adminteachview(request):
    view_id=teacherreg.objects.all()
    return render(request,'adminteachview.html',{'data':view_id})
def rejectt(request,id):
    a=get_object_or_404(teacherreg,id=id)
    a.delete()
    return redirect('adminteachview')
def rejects(request,id):
    a=get_object_or_404(Studentreg,id=id)
    a.delete()
    return redirect('adminstudview')


def teacherregister(request):
    if request.method == 'POST':
        form = teacherform(request.POST,request.FILES)
        logins = loginform(request.POST)
        print(form)
        if form.is_valid() and logins.is_valid():
            
            a = logins.save(commit=False)
            a.usertype = 2  
            a.save()
            b = form.save(commit=False)
            b.login_id = a  
            b.save()
            
            
            messages.success(request, "Form successfully submitted")
            return redirect('main') 
    else:
        form = teacherform()
        logins=loginform()
    return render(request,'teacherreg.html',{'form':form,'login':logins})
def login(request):
    if request.method == 'POST':
        form=login_check(request.POST)
        if form.is_valid():
            print('hiii')
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            try:
                user=Login.objects.get(email=email)
                if user.password==password:
                    if user.usertype==1:
                        request.session['stud_id']=user.id
                        return redirect('user')
                    elif user.usertype==2:
                        request.session['t_id']=user.id
                        return redirect('tuser')
                else:
                    messages.error(request,'invalid password')    
            except Login.DoesNotExist:
                messages.error(request,'User Does Not Exist')
    else:
        form=login_check()   
    return render(request,'login.html',{'login':form})
def sprofile(request):
    stud_id=request.session.get('stud_id')   
    login_details=get_object_or_404(Login,id=stud_id)
    stud=get_object_or_404(Studentreg,login_id=stud_id)
    if request.method=='POST':
        form=studentform(request.POST,instance=stud)
        form2=loginform(request.POST, instance=login_details)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return redirect('user')
    else:
        form=studentform(instance=stud)
        form2=loginform( instance=login_details)

    return render(request, 'sprofile.html',{'form':form,'form2':form2})

def tprofile(request):
    t_id=request.session.get('t_id')   
    login_details=get_object_or_404(Login,id=t_id)
    teacher=get_object_or_404(teacherreg,login_id=t_id)
    if request.method=='POST':
        form=teacherform(request.POST,instance=teacher)
        form2=loginform(request.POST, instance=login_details)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return redirect('tuser')
    else:
        form=teacherform(instance=teacher)
        form2=loginform( instance=login_details)

    return render(request, 'tprofile.html',{'form':form,'form2':form2})

def studentsview(request):
    view_id=Studentreg.objects.all()
    return render(request,'studentsview.html',{'data':view_id})

def search_student(request):
    query = request.GET.get('q', '') 
    results = Studentreg.objects.all()  

    if query:
        results = results.filter(
           Q(admno__icontains=query)|
           Q(name__icontains=query)|
           Q(department__icontains=query)  
        )

    return render(request, 'studentsview.html', {'results': results, 'query': query})

def teachersview(request):
    view_id=teacherreg.objects.all()
    print(view_id)
    return render(request,'teachersview.html',{'data':view_id})

def search_teacher(request):
    query = request.GET.get('q', '') 
    results = teacherreg.objects.all()  

    if query:
        results = results.filter(
           Q(tdepartment__icontains=query)|
           Q(tname__icontains=query)
        )

    return render(request, 'teachersview.html', {'results': results, 'query': query})

def uploadessay(request,id):
    stud_id=request.session.get('stud_id')   
    login_details=get_object_or_404(Login,id=stud_id)
    te_id=get_object_or_404(teacherreg,id=id)

    if request.method=='POST':
        form=essayuploadform(request.POST,request.FILES)
        if form.is_valid():
            a=form.save(commit=False)
            a.login_id=login_details
            a.tea_id=te_id
            a.save()
            return redirect('user')
    else:
        form=essayuploadform()
    return render(request, 'uploadessay.html',{'form':form})

def viewessay(request):
    stud_id=request.session.get('stud_id')
    login_details=get_object_or_404(Login,id=stud_id)
    view_id=Essay.objects.filter(login_id=login_details)
    return render(request,'viewessay.html',{'data':view_id})

def removeessay(request,id):
    a=get_object_or_404(Essay,id=id)
    a.delete()
    return redirect('viewessay')

def viewessayt(request):
    stud_id=request.session.get('stud_id')
    login_details=get_object_or_404(Login,id=stud_id)
    view_id=Essay.objects.all()
    essays_with_student_info = []

    for essay in view_id:
        student = Studentreg.objects.get(login_id=essay.login_id)
        essays_with_student_info.append({
            'essay': essay,
            'student_name': student.name,
            'student_admno': student.admno,
            'student_department': student.department,
            'student_semester': student.semester,

        })

    return render(request, 'viewessayt.html', {'essays_with_student_info': essays_with_student_info})

def uploadanswer(request,id):
    stud_id=request.session.get('stud_id')   
    login_details=get_object_or_404(Login,id=stud_id)
    tea_id=get_object_or_404(teacherreg,id=id)
    if request.method=='POST':
        form=answersheet(request.POST,request.FILES)
        if form.is_valid():
            a=form.save(commit=False)
            a.login_id=login_details
            a.t_id=tea_id
            a.save()
            return redirect('user')
    else:
        form=answersheet()
    return render(request, 'uploadanswer.html',{'form':form})
def viewanswer(request):
    stud_id=request.session.get('stud_id')
    login_details=get_object_or_404(Login,id=stud_id)
    view_id=Answer.objects.filter(login_id=login_details)
    return render(request,'viewanswer.html',{'data':view_id})
def removeanswer(request,id):
    a=get_object_or_404(Answer,id=id)
    a.delete()
    return redirect('viewanswer')
def viewanswert(request):
    tea_id=request.session.get('tea_id')
    login_details=get_object_or_404(teacherreg,login_id=tea_id)
    view_id=Answer.objects.filter(t_id = login_details)
   
    return render(request, 'viewanswert.html', {'view_ans': view_id})
