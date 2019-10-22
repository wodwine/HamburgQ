from django.contrib import admin

from .models import Quiz,Question

admin.site.register(Question)
admin.site.register(Quiz)
