from django.urls import path 
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.main, name='main'),
    path('login', views.login, name='login'),
    path('admin', views.admin, name='admin'),
    path('user', views.user, name='user'),
    path('tuser', views.tuser, name='tuser'),
    path('studentreg', views.studentreg, name='studentreg'),
    path('teacherreg', views.teacherregister, name='teacherreg'),
    path('adminstudview', views.adminstudview, name='adminstudview'),
    path('adminteachview', views.adminteachview, name='adminteachview'),
    path('rejectt/<int:id>', views.rejectt, name='rejectt'),
    path('rejects/<int:id>', views.rejects, name='rejects'),
    path('sprofile', views.sprofile, name='sprofile'),
    path('tprofile', views.tprofile, name='tprofile'),
    path('studentsview', views.studentsview, name='studentsview'),
    path('search_student', views.search_student, name='search_student'),
    path('uploadessay/<int:id>', views.uploadessay, name='uploadessay'),
    path('viewessay', views.viewessay, name='viewessay'),
    path('viewessayt', views.viewessayt, name='viewessayt'),
    path('removeessay/<int:id>', views.removeessay, name='removeessay'),
    path('uploadanswer/<int:id>', views.uploadanswer, name='uploadanswer'),
    path('viewanswer', views.viewanswer, name='viewanswer'),
    path('removeanswer/<int:id>', views.removeanswer, name='removeanswer'),
    path('viewanswert', views.viewanswert, name='viewanswert'),
    path('removeanswert/<int:id>', views.removeanswert, name='removeanswert'),
    path('teachersview', views.teachersview, name='teachersview'),
    path('search_teacher', views.search_teacher, name='search_teacher'),
    path('removeessayt/<int:id>', views.removeessayt, name='removeessayt'),
    path('uploadomr/<int:id>', views.uploadomr, name='uploadomr'),
    path('viewomr', views.viewomr, name='viewomr'),
    path('removeomr/<int:id>', views.removeomr, name='removeomr'),
    path('viewomrt', views.viewomrt, name='viewomrt'),
    path('removeomrt/<int:id>', views.removeomrt, name='removeomrt'),
    path('uploadassignment/<int:id>', views.uploadassignment, name='uploadassignment'),
    path('viewassignment', views.viewassignment, name='viewassignment'),
    path('removeassignment/<int:id>', views.removeassignment, name='removeassignment'),
    path('removeassignmentt/<int:id>', views.removeassignmentt, name='removeassignmentt'),
    path('viewassignmentt', views.viewassignmentt, name='viewassignmentt'),
    path('present/<int:id>/', views.present, name='present'),
    path('absent/<int:id>/', views.absent, name='absent'),
    path('viewattendance', views.viewattendance, name='viewattendance'),
    path('attendanceviewt', views.attendanceviewt, name='attendanceviewt'),
    path('adminsubjects', views.adminsubjects, name='adminsubjects'),
    path('subchoice', views.subchoice, name='subchoice'),
    path('viewsubject', views.viewsubject, name='viewsubject'),
    path('viewsubjectt/<int:id>', views.viewsubjectt, name='viewsubjectt'),
    path('uploadmarks', views.uploadmarks, name='uploadmarks'),
    path('upload-marks/<int:course_id>/<int:student_id>/', views.upload_internal_marks, name='internals'),


 ]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

 