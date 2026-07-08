from django.db import models

# Create your models here.
class Course(models.Model):
    course_code=models.CharField(max_length=10,unique=True)
    course_name=models.CharField(max_length=50)
    description=models.TextField(max_length=100)
    instructor=models.CharField(max_length=50)
    duration=models.IntegerField(help_text="duration in week")
    credit=models.IntegerField()
    
    