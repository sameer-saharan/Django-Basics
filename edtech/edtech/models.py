from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): 
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
        ('admin', 'Admin')
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class Course(models.Model): 
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    content = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'instructor'})

    def __str__(self): 
        return self.title

class Enrollment(models.Model): 
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)

class Assignment(models.Model): 
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()

class Submission(models.Model): 
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    file = models.FileField(upload_to='submission/')
    submitted_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model): 
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_msg')
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciever_msg')
    content = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)

class Announcement(models.Model): 
    title = models.CharField(max_length=100)
    maker = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': ['instructor', 'admin']})
    content = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)



