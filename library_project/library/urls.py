from django.urls import path
from .views import *

urlpatterns = [
    path('authors/', all_authors),
    path('books/', all_books),
    path('members/', all_members),
    path('create/', create),
    path('update/author/<int:id>/', update_author),
    path('update/book/<int:id>/', update_book),
    path('update/member/<int:id>/', update_member),
    path('delete/author/<int:id>/', delete_author),
    path('delete/book/<int:id>/', delete_book),
    path('delete/member/<int:id>/', delete_member),

    path('loans/', all_loans),
    path('create/loan/', create_loan),
    path('update/loan/<int:id>/', update_loan),

    path('authors/<int:id>/', author_details),
    path('members/<int:id>/', member_details),
    path('api/', BookAPI.as_view())
]
