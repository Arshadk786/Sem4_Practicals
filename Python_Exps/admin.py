'''
Experiment 09 : Creating web application using Django web framework to demonstrate functionality of user login and registration (also validating user detail using regular expression).
                                    Name : Khan Arshad Abdulla
                                    Roll No : 20CO24
                                    Academic Year : 2021-22
'''

from django.contrib import admin
from .models import Faculty , student_profile
# Register your models here.


admin.site.register(Faculty)
admin.site.register(student_profile)