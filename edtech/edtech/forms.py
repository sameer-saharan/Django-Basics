from django import forms
from .models import Course, Assignment, Submission, Message, Announcement

class CourseForm(forms.ModelForm):
    class Meta: 
        model = Course
        fields = ['title', 'description', 'content']

class AssignmentForm(forms.ModelForm): 
    class Meta: 
        model = Assignment
        fields = ['title', 'description']

class SubmissionForm(forms.ModelForm): 
    class Meta: 
        model = Submission
        fields = ['file']
    
class MessageForm(forms.ModelForm): 
    class Meta: 
        model = Message
        fields = ['content']

class AnnouncementForm(forms.ModelForm): 
    class Meta: 
        model = Announcement
        fields = ['title', 'content']