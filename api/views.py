from django.shortcuts import render
from django.http import JsonResponse

# For django_rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import BookSerializer
from .models import Book

# Create your views here.

@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'Books List': '/books/',
        'Book Selected': '/book_selected/<str:pk>/',
        'Add Book': '/book_add/',
        'Update Book': '/book-update/<str:pk>/',
        'Delete Book': '/book-delete/<str:pk>/'
    }
    
    return Response(api_urls)

@api_view(['GET'])
def bookList(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def bookSelected(request, pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(book, many=False)
    
    return Response(serializer.data)

@api_view(['POST'])
def bookAdd(request):

    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def bookUpdate(request, pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=book, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['Delete'])
def bookDelete(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()

    return Response('Book successfully deleted!')
