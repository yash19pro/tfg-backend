from django.urls import path

from . import views

urlpatterns = [
    path("person/", views.GetPerson.as_view(), name="person"),
    path("blog/", views.GetBlog.as_view(), name="blog")
]
