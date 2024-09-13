from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_courses, name='home'),
    path('courses/', views.show_courses, name='courses'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create/', views.course_create, name='course-create'),
    path('edit/<int:id>/', views.course_edit, name='course-edit'),
    path('delete/<int:id>/', views.course_delete, name='course-delete'),
    path('enroll/<int:id>', views.course_enroll, name='course-enroll'),
    path('content/<int:id>/', views.course_content, name='course-content'),
    path('announcement/', views.announcement, name='announcement')
]
