"""
URL configuration for student_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views,Hod_Views,Staff_Views,Student_Views
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),
    path('',views.LOGIN,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='logout'),

    #Profile Update
    path('Profile',views.PROFILE,name='profile'),
    path('Profile/update',views.PROFILE_UPDATE,name='profile_update'),

    #This is HOD panel url
    path('Hod/home',Hod_Views.HOME,name='hod_home'),
    path('Hod/Student/Add',Hod_Views.ADD_STUDENT,name='add_student'),
    path('Hod/Student/View',Hod_Views.VIEW_STUDENT,name='view_student'),
    path('Hod/Student/Edit/<str:id>',Hod_Views.EDIT_STUDENT,name='edit_student'),
    path('Hod/Student/Update',Hod_Views.UPDATE_STUDENT,name='update_student'),
    path('Hod/Student/Delete/<str:admin>',Hod_Views.DELETE_STUDENT,name='delete_student'),

    path('Hod/Staff/Add',Hod_Views.ADD_STAFF,name='add_staff'),
    path('Hod/Staff/View',Hod_Views.VIEW_STAFF,name='view_staff'),
    path('Hod/Staff/Edit/<str:id>',Hod_Views.EDIT_STAFF,name='edit_staff'),
    path('Hod/Staff/Update',Hod_Views.UPDATE_STAFF,name='update_staff'),
    path('Hod/Staff/Delete/<str:admin>',Hod_Views.DELETE_STAFF,name='delete_staff'),

    path('Hod/Course/Add',Hod_Views.ADD_COURSE,name='add_course'),
    path('Hod/Course/View',Hod_Views.VIEW_COURSE,name='view_course'),
    path('Hod/Course/Edit/<str:id>',Hod_Views.EDIT_COURSE,name='edit_course'),
    path('Hod/Course/Update',Hod_Views.UPDATE_COURSE,name='update_course'),
    path('Hod/Course/Delete/<str:id>',Hod_Views.DELETE_COURSE,name='delete_course'),

    path('Hod/Subject/Add',Hod_Views.ADD_SUBJECT,name='add_subject'),
    path('Hod/Subject/View',Hod_Views.VIEW_SUBJECT,name='view_subject'),
    path('Hod/Subject/Edit/<str:id>',Hod_Views.EDIT_SUBJECT,name='edit_subject'),
    path('Hod/Subject/Update',Hod_Views.UPDATE_SUBJECT,name='update_subject'),
    path('Hod/Subject/Delete/<str:id>',Hod_Views.DELETE_SUBJECT,name='delete_subject'),



    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

