from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Course, Enrollment, Assignment, Submission, Message, Announcement
from .forms import CourseForm, AssignmentForm, SubmissionForm, MessageForm, AnnouncementForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def user_login(request): 
    if request.method == 'POST': 
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid(): 
            user = form.get_user()
            login(request, user)
            return redirect('home')
    
    else: 
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request): 
    logout(request)
    return render(request, 'logout.html')

def show_courses(request): 
    courses = Course.objects.all()
    enrolled_courses = Enrollment.objects.filter(student=request.user).values_list('course_id', flat=True)
    return render(request, 'courses.html', {'courses': courses, 'enrolled_courses': enrolled_courses})

@login_required
def course_enroll(request, id): 
    course = get_object_or_404(Course, pk=id)
    return render(request, 'course_enroll.html', {'course': course})

@login_required
def course_create(request): 
    if request.method == 'POST': 
        form = CourseForm(request.POST)
        if form.is_valid(): 
            course = form.save(commit=False)
            course.instructor = request.user
            course.save()
            return redirect('home')
    
    else: 
        form = CourseForm()
    
    return render(request, 'create_course.html', {'form': form})

@login_required
def course_edit(request, id): 
    if request.user.role not in ['instructor', 'admin']:
        return HttpResponse("You are not authorized")
    
    course = get_object_or_404(Course, pk=id)
    if request.method == 'POST': 
        form = CourseForm(request.POST, instance=course)
        if form.is_valid(): 
            form.save()
            return redirect('home')
    
    else: 
        form = CourseForm(instance=course)
    
    return render(request, 'edit_course.html', {'form': form, 'course': course})

@login_required
def course_delete(request, id): 
    if request.user.role not in ['admin']:
        return HttpResponse("You are not authorized")
    
    course = get_object_or_404(Course, pk=id)
    if request.method == 'POST': 
        course.delete()
        return redirect('courses')
    
    return render(request, 'delete.html', {'course': course})

@login_required
def course_enroll(request, id):
     if request.user.role not in ['student']:
        return HttpResponse("You are not authorized")
     
     course = get_object_or_404(Course, pk=id)
     Enrollment.objects.get_or_create(student=request.user, course=course)
     return redirect('courses')

@login_required
def course_content(request, id): 
    if request.user.role not in ['instructor', 'admin', 'student']: 
        return HttpResponse("You are not authorized to view this content")
    
    course = get_object_or_404(Course, pk=id)
    is_enrolled = Enrollment.objects.filter(student=request.user, course=course).exists()

    if not is_enrolled: 
        return HttpResponse("You have not enrolled in this course, Kindly Enroll in the course to view full content")
    
    return render(request, 'course_content.html', {'course': course})

@login_required
def announcement(request):
    announcements = Announcement.objects.all()

    if request.method == 'POST': 
        form = AnnouncementForm(request.POST)
        if form.is_valid(): 
            announcement = form.save(commit=False)
            announcement.maker = request.user
            announcement.save()
            return redirect('announcement')
        
    else: 
        form = AnnouncementForm()
    
    return render(request, 'announce.html', {'form': form, 'announcements': announcements})