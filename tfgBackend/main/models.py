import datetime

from django.contrib.auth.models import User
from django.db import models


class University(models.Model):
    name = models.CharField(max_length=100)


class Stream(models.Model):
    name = models.CharField(max_length=20)


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    batch = models.IntegerField(default=-1)
    role = models.CharField(max_length=10)


class Tag(models.Model):
    name = models.CharField(max_length=50)
    count = models.IntegerField(default=0)


class Question(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='main/question_images/', null=True)
    date_posted = models.DateTimeField(default=datetime.datetime.now)
    votes = models.IntegerField(default=0)


class Answer(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='main/answer_images/', null=True)
    date_posted = models.DateTimeField(default=datetime.datetime.now)
    votes = models.IntegerField(default=0)


class Blog(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='main/blog_images/', null=True)
    date_posted = models.DateTimeField(default=datetime.datetime.now)
    votes = models.IntegerField(default=0)


class BlogComment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=datetime.datetime.now)


class TechStack(models.Model):
    name = models.CharField(max_length=50)


class Project(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='main/project_images/', null=True)
    date_posted = models.DateTimeField(default=datetime.datetime.now)
    tech_stack = models.ManyToManyField(TechStack)


class ProjectComment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=datetime.datetime.now)
