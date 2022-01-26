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


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = otherDetails
        fields = ('id', 'address', 'phonenumber', 'user', 'city')
