from django.urls import path

from . import views

urlpatterns = [
    path('blog/', views.fetch_blogs, name="blog"),
    path('project/', views.fetch_projects, name="project"),
    path('question/', views.fetch_questions, name="question"),
]
