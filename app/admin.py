from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class UserModel(UserAdmin):
    list_display = ['username','user_type']
    
admin.site.register(CustomUser, UserModel) 

# Register Course and session year model

admin.site.register(Course)
admin.site.register(Session_Year)

# Register Student Model
admin.site.register(Student)

# Register Staff Model
admin.site.register(Staff)

# Register Subject Model
admin.site.register(Subject)