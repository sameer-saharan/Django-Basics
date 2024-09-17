from django.db import models

class Author(models.Model): 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()
    biography = models.TextField()
   
class Book(models.Model): 
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()
    number_of_pages = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Member(models.Model): 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    membership_date = models.DateField()
    email = models.EmailField(unique=True)

class Loan(models.Model): 
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_date = models.DateField()
    return_date = models.DateField(null=True)

