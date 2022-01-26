from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializer import BlogSerializer, PersonSerializer


class GetPerson(APIView):
    @staticmethod
    def get(request):
        list1 = Person.objects.all()
        print(list1)
        serializer = PersonSerializer(list1, many=True)
        return Response(serializer.data)


class GetBlog(APIView):
    @staticmethod
    def get(request):
        list1 = Blog.objects.all()
        print(list1)
        serializer = BlogSerializer(list1, many=True)
        return Response(serializer.data)
