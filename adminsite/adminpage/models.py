from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length = 100)
    middle_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    student_number = models.CharField(max_length = 9)
    inTheBldg = models.BooleanField(default = False)

    def __str__(self):
        return self.first_name + ' ' + self.middle_name[0] + '. '+ self.last_name

class timeIn(models.Model):
    timestamp = models.DateTimeField()
    student = models.ForeignKey(Student, on_delete = models.CASCADE)

class timeOut(models.Model):
    timestamp = models.DateTimeField()
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
