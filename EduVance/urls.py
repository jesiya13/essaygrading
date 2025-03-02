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
    path('teachersview', views.teachersview, name='teachersview'),
    path('search_teacher', views.search_teacher, name='search_teacher'),

 ]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

 