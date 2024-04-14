from django.contrib import admin
from .models import User,Task

admin.site.register(User)
class Task_admin(admin.ModelAdmin):
    list_display=[
        'user','task','task_type'
        
    ]   
admin.site.register(Task,Task_admin)