from django.contrib import admin
from .models import Lesson


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'author', 'is_approved', 'id_rejected', 'datetime']
    list_display_links = ['id', '__str__']


admin.site.register(Lesson, LessonAdmin)
