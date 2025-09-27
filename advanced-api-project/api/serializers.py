from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone

class AuthorSerializer(serializers.ModelSerializer):
    """This is the Author serializer"""
    
    class Meta:
        model = Author
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    """This is the Book serializer"""
    name = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['name', 'title', 'publication_year', 'author']

    def validate(self, data):
        if data('publication_year') > timezone.now().date():
            raise serializers.ValidationError("Publication Year must be an int that is 4 int")
        return data