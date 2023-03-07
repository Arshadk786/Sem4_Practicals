'''
Experiment 09 : Creating web application using Django web framework to demonstrate functionality of user login and registration (also validating user detail using regular expression).
                                    Name : Khan Arshad Abdulla
                                    Roll No : 20CO24
                                    Academic Year : 2021-22
'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path ('register', views.register , name='register'),
    path ('login', views.login1  , name='login'),
    
    # path ('store',views.home,name='store'),
    path ('faculty',views.faculty,name='faculty'),
    path('student_profiler/<int:id>',views.student_profiler,name='student_profiler'),
    path('faculty_view/<str:Roll_no>', views.faculty_view , name='faculty_view'),
    path('logout',views.logout_user,name='logout')
]
