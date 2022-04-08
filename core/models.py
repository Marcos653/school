from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    
    def __str__(self):
        return self.name

class Student(models.Model):        
    name = models.CharField(max_length=255, null=False, blank=False)
    total = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Quizz(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=False, blank=False)
    text = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.text       

class Answer(models.Model):
    quizz = models.ForeignKey(Quizz, on_delete=models.CASCADE, null=False, blank=False)
    text = models.CharField(max_length=255, null=False, blank=False)      
    valid = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class StudentPoint(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False, blank=False)
    point = models.IntegerField(default=0)

    def __str__(self):
        return self.student.name

def post_point(sender, instance, created, **kwargs):
    if created:
        print('oiiiiiiiiiiiiiiiiiiii')
        # points = StudentPoint.objects.filter(point=1)
        # all_point = points.count()
        instance.student.total += 1
        instance.student.save()

post_save.connect(post_point, StudentPoint)
