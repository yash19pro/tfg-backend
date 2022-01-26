import json

from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse

from .models import *


def fetch_blogs(request):
    if request.method == "GET":
        d = dict(request.GET)
        filter = d["tag"]
        print(filter)

        blogs = Blog.objects.all()

        res = []
        for blog_object in blogs:
            tags = []
            for tag in blog_object.tags.all():
                tmp = {
                    "tag": tag.name,
                    "count": tag.count
                }
                tags.append(tmp)

            comments = []
            cmts = BlogComment.objects.filter(blog__pk=blog_object.pk)
            for comment_object in cmts:
                tmp = {
                    "user": comment_object.user.username,
                    "text": comment_object.comment,
                    "datePublished": str(comment_object.date_posted)

                }
                comments.append(tmp)

            scheme = request.is_secure() and "https" or "http"
            tmp = {
                "id": blog_object.id,
                "img": f'{scheme}://{request.get_host()}' + blog_object.image.url,
                "author": blog_object.person.username,
                "title": blog_object.title,
                "datePublished": str(blog_object.date_posted),
                "content": blog_object.content,
                "votes": blog_object.votes,
                "tags": tags,
                "comments": comments
            }
            res.append(tmp)

        return JsonResponse({"data": res})
