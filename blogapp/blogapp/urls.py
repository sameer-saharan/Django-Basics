from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('accounts/profile/', views.profile),
    path('blog/', views.showBlogList, name='bloglist'),
    path('blog/<int:id>/', views.showBlogDetails, name='details'),
    path('', views.blog_list, name='home'),
    path('comment/<int:id>/', views.add_comment, name='add_comment'),
    path('create/', views.create_post, name='create_post'),
    path('edit/<int:id>/', views.edit_post, name='edit_post'),
    path('delete/<int:id>/', views.delete_post, name='delete_post')

]
