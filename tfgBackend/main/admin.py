from django.contrib import admin

from .models import (Answer, Blog, BlogComment, Person, Project,
                     ProjectComment, Question, Stream, Tag, TechStack,
                     University)

admin.site.register(University)
admin.site.register(Stream)
admin.site.register(Person)
admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Blog)
admin.site.register(BlogComment)
admin.site.register(TechStack)
admin.site.register(Project)
admin.site.register(ProjectComment)
