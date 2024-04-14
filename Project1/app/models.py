from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=25)
    email=models.EmailField()
    mobile=models.IntegerField()
    def __str__(self):
        return self.name
choice=[
    ('PENDING','pending'),
    ('DONE','done')
]
class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    task=models.TextField()
    task_type=models.CharField(max_length=10,choices=choice,default='pending')
    def __str__(self):
        return self.task