from django.contrib import admin
from .models import User, Course, Announcement

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Announcement)