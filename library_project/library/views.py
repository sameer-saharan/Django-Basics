from django.shortcuts import render
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

#API View
class BookAPI(APIView): 
    def get(self, request): 
        books = Book.objects.all()
        books_sr = BookSerializer(books, many=True)
        return Response({'status': 200, 'books': books_sr.data})
    
    def post(self, request): 
        book_sr = BookSerializer(data=request.data)
        if not book_sr.is_valid(): 
            return Response({'status': 403, "errors": book_sr.errors, 'message': 'Something went wrong- Book'})
        
        book_sr.save()
        return Response({'status': 200, 'book_data': book_sr.data})

    def patch(self, request): 
        try: 
            book = Book.objects.get(pk=request.data['id'])
        except Book.DoesNotExist(): 
            return Response({'status': 403, 'message': 'Book does not exist'})
    
        book_sr = BookSerializer(book, data=request.data, partial=True)
        if not book_sr.is_valid(): 
            return Response({'status': 403, 'message': "Book Serializer is not valid"})
    
        book_sr.save()
        return Response({'status': 200, 'book': book_sr.data})
    
    def delete(self, request): 
        try: 
            book = Book.objects.get(pk=request.data['id'])
        except Book.DoesNotExist(): 
            return Response({'status': 403, 'message': 'Book does not exist'})
    
        book.delete()
        return Response({'status': 200, 'message': "Book deleted successfully"})


@api_view(['GET'])
def all_authors(request): 
    authors = Author.objects.all()
    authors_sr = AuthorSerializer(authors, many=True)
    return Response({'status': 200, 'authors': authors_sr.data})

@api_view(['GET'])
def all_books(request): 
    books = Book.objects.all()
    books_sr = BookSerializer(books, many=True)
    return Response({'status': 200, 'books': books_sr.data})

@api_view(['GET'])
def all_members(request): 
    members = Member.objects.all()
    members_sr = MemberSerializer(members, many=True)
    return Response({'status': 200, 'members': members_sr.data})

@api_view(['POST'])
def create(request): 
    data = request.data 

    author_data = data.get('author')
    book_data = data.get('book')
    member_data = data.get('member')

    if author_data: 
        author_sr = AuthorSerializer(data=author_data)

        if not author_sr.is_valid(): 
            return Response({'status': 403, 'message': 'Something went wrong- Author'})

        author_sr.save()
        return Response({'status': 200, 'author_data': author_sr.data})
    
    if book_data: 
        book_sr = BookSerializer(data=book_data)

        if not book_sr.is_valid(): 
            return Response({'status': 403, "errors": book_sr.errors, 'message': 'Something went wrong- Book'})
        
        book_sr.save()
        return Response({'status': 200, 'book_data': book_sr.data})
    
    if member_data: 
        member_sr = MemberSerializer(data=member_data)

        if not member_sr.is_valid(): 
            return Response({'status': 403, 'message': 'Something went wrong- Member'})
        
        member_sr.save()
        return Response({'status': 200, 'member_data': member_sr.data})


@api_view(['PUT'])
def update_author(request, id): 
    try: 
        author = Author.objects.get(pk=id)
    except Author.DoesNotExist(): 
        return Response({'status': 403, 'message': 'Author does not exist'})

    author_sr = AuthorSerializer(author, data=request.data)
    if not author_sr.is_valid(): 
        return Response({'status': 403, 'message': "Author Serializer is not valid"})
    
    author_sr.save()
    return Response({'status': 200, 'author': author_sr.data})

@api_view(['PUT'])
def update_book(request, id): 
    try: 
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist(): 
        return Response({'status': 403, 'message': 'Book does not exist'})
    
    book_sr = BookSerializer(book, data=request.data)
    if not book_sr.is_valid(): 
        return Response({'status': 403, 'message': "Book Serializer is not valid"})
    
    book_sr.save()
    return Response({'status': 200, 'book': book_sr.data})

@api_view(['PUT'])
def update_member(request, id): 
    try: 
        member = Member.objects.get(pk=id)
    except Member.DoesNotExist(): 
        return Response({'status': 403, 'message': 'Member does not exist'})
    
    member_sr = MemberSerializer(member, data=request.data)
    if not member_sr.is_valid(): 
        return Response({'status': 403, 'message': "Member Serializer is not valid"})
    
    member_sr.save()
    return Response({'status': 200, 'member': member_sr.data})

@api_view(['DELETE']) 
def delete_author(request, id): 
    try: 
        author = Author.objects.get(pk=id)
    except Author.DoesNotExist(): 
        return Response({'status': 403, 'message': 'Author does not exist'})
    
    author.delete()
    return Response({'status': 200, 'message': "Author deleted successfully"})

@api_view(['DELETE'])
def delete_book(request, id): 
    try: 
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist(): 
        return Response({'status': 403, 'message': 'Book does not exist'})
    
    book.delete()
    return Response({'status': 200, 'message': "Book deleted successfully"})

@api_view(['DELETE'])
def delete_member(request, id): 
    try: 
        member = Member.objects.get(pk=id)
    except Member.DoesNotExist(): 
        return Response({'status': 403, 'message': 'Member does not exist'})
    
    member.delete()
    return Response({'status': 200, 'message': "Member deleted successfully"})

@api_view(['GET'])
def all_loans(request): 
    loans = Loan.objects.all()
    loans_sr = LoanSerializer(loans, many=True)
    return Response({'status': 200, 'loans': loans_sr.data})

@api_view(['POST'])
def create_loan(request): 
    loan_sr = LoanSerializer(data=request.data)

    if not loan_sr.is_valid(): 
        return Response({'status': 403, 'message': 'Loan Serializer not valid'})
    
    loan_sr.save()
    return Response({'status': 200, 'loan': loan_sr.data})

#Updating Loan return_date
@api_view(['PATCH'])
def update_loan(request, id): 
    try: 
        loan = Loan.objects.get(pk=id)
    except Loan.DoesNotExist(): 
        return Response({'status': 403, 'message': 'Loan does not exist'})
    
    loan_sr = LoanSerializer(loan, data=request.data, partial=True)
    if not loan_sr.is_valid(): 
        return Response({'status': 403, 'message': 'Loan Serializer not valid'})
    
    loan_sr.save()
    return Response({'status': 200, 'loan': loan_sr.data})

# List of Books by Author
@api_view(['GET'])
def author_details(request, id): 
    author = Author.objects.get(pk=id)
    author_sr = AuthorSerializer(author)
    books = Book.objects.filter(author=author)
    books_sr = BookSerializer(books, many=True)
    return Response({'status': 200,'author': author_sr.data ,'books_written': books_sr.data})

#List of Loans by Member
@api_view(['GET'])
def member_details(request, id): 
    member = Member.objects.get(pk=id)
    member_sr = MemberSerializer(member)
    loans = Loan.objects.filter(member=member)
    loans_sr = LoanSerializer(loans, many=True)
    return Response({'status': 200, 'member': member_sr.data, 'loans': loans_sr.data})