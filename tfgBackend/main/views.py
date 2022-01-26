import json

from django.conf import settings
from django.shortcuts import render

from .models import *


def fetch_blogs(request):
    if request.method == "GET":
        blogs = Blog.objects.all()

        res = []
        for blog in blogs:
            tmp = {
                "id": blog.id,
                "img": settings.MEDIA_URL + blog.image.url,
                "author": blog.person.user.username,
                "title"
                "description"
                ""
            }
