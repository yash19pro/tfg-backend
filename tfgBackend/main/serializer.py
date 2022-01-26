from rest_framework import serializers

from .models import *


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ("name")


class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fields = ("name")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        field = ("name", "count")


class PersonSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username')

    class Meta:
        model = Person
        fields = ("user_name", "university", "stream", "batch", "role")


class BlogSerializer(serializers.ModelSerializer):
    tag = TagSerializer(read_only=True, many=True)
    # print(tag)

    class Meta:
        model = Blog
        fields = '__all__'
