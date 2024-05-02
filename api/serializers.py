from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        # attributes to serialize
        model = Book
        fields = '__all__'
    
