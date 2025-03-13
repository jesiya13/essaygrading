from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages
from django.db.models import Q
from datetime import date 
from django.http import JsonResponse


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
        form=studentform(request.POST,request.FILES,instance=stud)
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
        form=teacherform(request.POST,request.FILES,instance=teacher)
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
   tea_id=request.session.get('t_id')
   login_details=get_object_or_404(teacherreg,login_id=tea_id)
   view_id=Essay.objects.filter(tea_id = login_details).select_related('login_id__student_as_loginid')
   return render(request, 'viewessayt.html', {'view_essay': view_id})

def removeessayt(request,id):
    b=get_object_or_404(Essay,id=id)
    b.delete()
    return redirect('viewessayt')



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
    tea_id=request.session.get('t_id')
    login_details=get_object_or_404(teacherreg,login_id=tea_id)
    view_id=Answer.objects.filter(t_id = login_details).select_related('login_id__student_as_loginid')
   
    return render(request, 'viewanswert.html', {'view_ans': view_id})

def removeanswert(request,id):
    b=get_object_or_404(Answer,id=id)
    b.delete()
    return redirect('viewanswert')

def uploadomr(request,id):
    stud_id=request.session.get('stud_id')   
    login_details=get_object_or_404(Login,id=stud_id)
    tc_id=get_object_or_404(teacherreg,id=id)
    if request.method=='POST':
        form=omr(request.POST,request.FILES)
        if form.is_valid():
            a=form.save(commit=False)
            a.login_id=login_details
            a.tc_id=tc_id
            a.save()
            return redirect('user')
    else:
        form=omr()
    return render(request, 'uploadomr.html',{'form':form})

def viewomr(request):
    stud_id=request.session.get('stud_id')
    login_details=get_object_or_404(Login,id=stud_id)
    view_id=Omr.objects.filter(login_id=login_details)
    return render(request,'viewomr.html',{'data':view_id})

def removeomr(request,id):
    a=get_object_or_404(Omr,id=id)
    a.delete()
    return redirect('viewomr')

def viewomrt(request):
    tea_id=request.session.get('t_id')
    login_details=get_object_or_404(teacherreg,login_id=tea_id)
    view_id=Answer.objects.filter(t_id = login_details).select_related('login_id__student_as_loginid')
   
    return render(request, 'viewomrt.html', {'view_omr': view_id})

def removeomrt(request,id):
    b=get_object_or_404(Omr,id=id)
    b.delete()
    return redirect('viewomrt')

def uploadassignment(request,id):
    stud_id=request.session.get('stud_id')   
    login_details=get_object_or_404(Studentreg,login_id=stud_id)
    tc_id=get_object_or_404(teacherreg,id=id)
    if request.method=='POST':
        form=assignment(request.POST,request.FILES)
        if form.is_valid():
            a=form.save(commit=False)
            a.login_id=login_details
            a.ta_id=tc_id
            a.save()
            return redirect('user')
    else:
        form=assignment()
    return render(request, 'uploadassignment.html',{'form':form})

def viewassignment(request):
    stud_id=request.session.get('stud_id')
    login_details=get_object_or_404(Studentreg,login_id=stud_id)
    view_id=Assignment.objects.filter(login_id=login_details)

    return render(request,'viewassignment.html',{'data':view_id})

def removeassignment(request):
    stud_id=request.session.get('stud_id')
    login_details=get_object_or_404(Login,id=stud_id)
    view_id=Assignment.objects.filter(login_id=login_details)
    return render(request,'viewassignment.html',{'data':view_id})

def viewassignmentt(request):
    tea_id = request.session.get('t_id')
    login_details = get_object_or_404(teacherreg, login_id=tea_id)
    view_id = Assignment.objects.filter(ta_id=login_details).select_related('login_id') 
    results = view_id 
    query = request.GET.get('q', '') 
    if query:
        results = view_id.filter(
           Q(login_id__admno__icontains=query) |
           Q(login_id__name__icontains=query) |
           Q(login_id__department__icontains=query)
        )
    return render(request, 'viewassignmentt.html', {'view_assignment': results, 'query':query})

def removeassignmentt(request,id):
    b=get_object_or_404(Assignment,id=id)
    b.delete()
    return redirect('viewassignmentt')

def viewattendance(request):
    form=attendance()
    dept = request.GET.get('department') 
    sem = request.GET.get('semester') 
    results = Studentreg.objects.filter(department=dept,semester=sem) 
    if results:
        return render(request, 'attendancetable.html',{'results':results})
    print(results)
    return render(request, 'attendance.html',{'form':form})

def present(request,id):
    a=get_object_or_404(Studentreg,id=id)
    tea_id = request.session.get('t_id')
    login_details = get_object_or_404(teacherreg, login_id=tea_id)
    if Attendance.objects.filter(t_id= login_details,login_id=a,present=1,current_date=date.today()).exists():
        return JsonResponse({'status': 'error', 'message': ' Attendance Already marked for today!'})
    else:
        Attendance.objects.create(t_id= login_details,login_id=a,present=1)
        return JsonResponse({'status': 'success', 'message': 'Attendance marked Now!'})


def absent(request,id):
    a=get_object_or_404(Studentreg,id=id)
    tea_id = request.session.get('t_id')
    login_details = get_object_or_404(teacherreg, login_id=tea_id)
    if Attendance.objects.filter(t_id= login_details,login_id=a,absent=2,current_date=date.today()).exists():
        return JsonResponse({'status': 'error', 'message': ' Attendance Already marked for today!'})
    else:
        Attendance.objects.create(t_id= login_details,login_id=a,absent=2)
        return JsonResponse({'status': 'success', 'message': 'Attendance marked Now!'})

def attendanceviewt(request):
    form=attendanceview()
    date = request.GET.get('date') 
    results = Attendance.objects.filter(current_date=date,present=1) 
    if results:
        return render(request, 'attendancet.html',{'results':results})
    print(results)
    return render(request,'checkattendance.html',{'form':form})

def markupload(request):
    form=attendance()
    dept = request.GET.get('department') 
    sem = request.GET.get('semester') 
    results = Studentreg.objects.filter(department=dept,semester=sem) 
    if results:
        return render(request, 'attendancetable.html',{'results':results})
    print(results)
    return render(request, 'attendance.html',{'form':form})


def adminsubjects(request):
    if request.method == 'POST':
        dept = request.POST.get('dept')
        sem = request.POST.get('sem')
        courses = request.POST.getlist('courses[]')  # Get all courses
        elective_courses = request.POST.getlist('elective_courses[]')  # Get electives

        if len(elective_courses) != 3:  # Ensure exactly 3 elective courses
            messages.error(request, "You must enter exactly 3 elective courses.")
            return redirect('admin')

        # Create Subject (semester)
        subject = Subject.objects.create(dept=dept, sem=sem)

        # Save each regular course
        for course_name in courses:
            if course_name.strip():
                Course.objects.create(subject=subject, name=course_name)

        # Save exactly 3 elective courses
        for elective_name in elective_courses:
            if elective_name.strip():
                ElectiveCourse.objects.create(subject=subject, name=elective_name)

        messages.success(request, "Subject and courses added successfully.")
        return redirect('admin')

    else:
        form = SubjectForm()  
    return render(request, 'subjects.html', {'form': form})

# def subchoice(request):
#     stud_id = request.session.get('stud_id')
#     login_details = get_object_or_404(Studentreg, login_id=stud_id)
#     semester=login_details.semester
#     print(semester)
#     return render(request, 'subchoicestud.html')


def subchoice(request):
    stud_id = request.session.get('stud_id')  # Get student ID from session
    student = get_object_or_404(Studentreg, login_id=stud_id)  # Fetch student

    if request.method == 'POST':
        form = ElectiveForm(request.POST, student=student)
        if form.is_valid():
            # Ensure student hasn't already selected an elective for the semester
            if SubjectView.objects.filter(stud_id=student, semester=student.semester).exists():
                return render(request, 'subchoicestud.html', {
                    'form': form, 
                    'error': 'You have already selected an elective for this semester!'
                })

            # Save elective choice
            subject_view = form.save(commit=False)
            subject_view.stud_id = student
            subject_view.semester = student.semester
            subject_view.save()
            return redirect('user')  # Redirect to success page after submission

    else:
        form = ElectiveForm(student=student)

    return render(request, 'subchoicestud.html', {'form': form})

def uploadmarks(request):
    form=uploadmark()
    dept = request.GET.get('department') 
    sem = request.GET.get('semester') 
    results = Studentreg.objects.filter(department=dept,semester=sem) 
    if results:
        return render(request, 'markuploadviewt.html',{'results':results})
    print(results)
    return render(request, 'markupload.html',{'form':form})



def upload_internal_marks(request, course_id, student_id):
    # Fetch the course, student, and subject
    course = get_object_or_404(Course, id=course_id)
    student = get_object_or_404(Studentreg, id=student_id)
    subject = course.id  # Fetch the correct subject from the course
    logid = request.session.get('t_id')
    teacher_id = get_object_or_404(teacherreg, login_id=logid)

    # Check if marks already exist for this student and subject
    existing_marks = InternalMarks.objects.filter(subject=subject, stud_id=student).exists()

    if request.method == 'POST':
        marks = request.POST.get('marks')  # Get the marks from the form input

        # Validate marks (ensure it's a numeric value)
        if not marks.isdigit():
            messages.error(request, "Marks must be a numeric value.")
            return redirect('internals', course_id=course_id, student_id=student_id)

        marks = int(marks)  # Convert marks to integer

        if existing_marks:
            # If marks already exist for the student and subject, prevent duplicate entry
            messages.error(request, 'Marks for this student in this subject already exist.')
        else:
            # Create a new entry
            InternalMarks.objects.create(subject_id=subject, stud_id=student, marks=marks, login_id=teacher_id)
            messages.success(request, 'Marks uploaded successfully!')

        return redirect('viewsubjectt', student.id)  # Redirect after saving

    # If GET request, render the form
    return render(request, 'uploadmark_teacher.html', {'course': course, 'student': student})

def upload_internal_marks_elective(request, course_id, student_id):
    # Fetch the course, student, and subject
    course = get_object_or_404(ElectiveCourse, id=course_id)
    student = get_object_or_404(Studentreg, id=student_id)
    subject = course.id  # Fetch the correct subject from the course
    logid = request.session.get('t_id')
    teacher_id = get_object_or_404(teacherreg, login_id=logid)

    # Check if marks already exist for this student and subject
    existing_marks = InternalMarks.objects.filter(subject=subject, stud_id=student).exists()

    if request.method == 'POST':
        marks = request.POST.get('marks')  # Get the marks from the form input

        # Validate marks (ensure it's a numeric value)
        if not marks.isdigit():
            messages.error(request, "Marks must be a numeric value.")
            return redirect('internals', course_id=course_id, student_id=student_id)

        marks = int(marks)  # Convert marks to integer

        if existing_marks:
            # If marks already exist for the student and subject, prevent duplicate entry
            messages.error(request, 'Marks for this student in this subject already exist.')
        else:
            # Create a new entry
            InternalMarks.objects.create(subject_id=subject, stud_id=student, marks=marks, login_id=teacher_id)
            messages.success(request, 'Marks uploaded successfully!')

        return redirect('viewsubjectt', student.id)  # Redirect after saving

    # If GET request, render the form
    return render(request, 'uploadmark_teacher.html', {'course': course, 'student': student})


def viewsubject(request):
    # Get the student ID from the session (assuming the user is linked to the Studentreg model)
    student_id = request.session.get('stud_id')
    st = get_object_or_404(Studentreg, login_id=student_id)

    # Get all subjects for the student based on their department and semester
    subjects = Subject.objects.filter(dept=st.department, sem=st.semester)

    # Get all the courses (core subjects) for the student's semester
    courses = Course.objects.filter(subject__in=subjects)

    # Get the electives selected by the student for the current semester from the SubjectView model
    selected_electives = SubjectView.objects.filter(stud_id=st, semester=st.semester)
    electives = ElectiveCourse.objects.filter(name__in=[selection.elective_course for selection in selected_electives])

    # Get the student's marks for the courses and electives from the InternalMarks model
    course_marks = InternalMarks.objects.filter(stud_id=st.id, subject__in=[course.id for course in courses])
    elective_marks = InternalMarks.objects.filter(stud_id=st.id, subject__in=[elective.id for elective in electives])

    # Attach marks to courses and electives
    for course in courses:
        course.marks = None  # Default to None if no marks found
        for mark in course_marks:
            if mark.subject == course:
                course.marks = mark.marks
                break

    for elective in electives:
        elective.marks = None  # Default to None if no marks found
        for mark in elective_marks:
            if mark.subject == elective:
                elective.marks = mark.marks
                break

    # Pass the data to the template
    return render(request, 'viewsubject.html', {
        'student': st,  # Pass the student details
        'courses': courses,
        'electives': electives,
    })

# def viewsubjectt(request, id):
#     student = get_object_or_404(Studentreg, id=id)

#     # Check if data is being returned
#     core_subjects = Course.objects.filter(subject__dept=student.department, subject__sem=student.semester)
#     print("Core Subjects:", core_subjects)  # Debugging line

#     electives = SubjectView.objects.filter(stud_id=student, semester=student.semester)
#     print("Electives:", electives)  # Debugging line

#     view_sub = ElectiveCourse.objects.filter(name__in=[elective.elective_course for elective in electives])
#     print("View Sub:", view_sub)  # Debugging line

#     internal_marks = InternalMarks.objects.filter(stud_id=student)
#     print("Internal Marks:", internal_marks)  # Debugging line

#     return render(request, 'viewsubjectt.html', {
#         'studentid': student.id,
#         'core_subjects': core_subjects,
#         'view_sub': view_sub,
#         'internal_marks': internal_marks,
#     })

def viewsubjectt(request,id):

    student = get_object_or_404(Studentreg, id=id)

    core_subjects = Course.objects.filter(subject__dept=student.department, subject__sem=student.semester)
    electives = SubjectView.objects.filter(stud_id=student, semester=student.semester)
    view_sub = ElectiveCourse.objects.filter(name__in=[elective.elective_course for elective in electives])

    internal_marks = InternalMarks.objects.filter(stud_id=student)
    # print(internal_marks)
    return render(request, 'viewsubjectt.html', {
        'studentid': student.id,
        'core_subjects': core_subjects,
        'view_sub': view_sub,
        'internal_marks': internal_marks,
    })

# def viewsubjectt(request, id):
#     # Get student details
#     student = get_object_or_404(Studentreg, id=id)

#     # Get the subject (based on department & semester)
#     subject = get_object_or_404(Subject, dept=student.department, sem=student.semester)

#     # Fetch core subjects
#     core_subjects = Course.objects.filter(subject=subject)

#     # Fetch electives chosen by student
#     selected_electives = SubjectView.objects.filter(stud_id=student)

#     # Fetch internal marks for the student
#     internal_marks = InternalMarks.objects.filter(stud_id=student)

#     return render(request, 'viewsubjectt.html', {
#         'core_subjects': core_subjects,
#         'view_sub': selected_electives,  # Corrected this line
#         'internal_marks': internal_marks,
#         'studentid': id  # Use id, not undefined student_id
#     })

def promote(request,id):
    student = get_object_or_404(Studentreg, id=id)
    sem=student.semester
    student.semester=sem+1
    student.save()
    
    return redirect('adminstudview')

def demote(request,id):
    student = get_object_or_404(Studentreg, id=id)
    sem=student.semester
    student.semester=sem-1
    student.save()
    
    return redirect('adminstudview')





