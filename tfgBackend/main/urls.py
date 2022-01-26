from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.fetch_blogs, name="blog"),
]
