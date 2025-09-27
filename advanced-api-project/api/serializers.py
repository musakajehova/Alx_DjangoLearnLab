from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    """This is the Book serializer"""
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        if data('publication_year') > timezone.now().date():
            raise serializers.ValidationError("Publication Year must be an int that is 4 int")
        return data

class AuthorSerializer(serializers.ModelSerializer):
    """This is the Author serializer"""
    name = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['author', 'name']


    