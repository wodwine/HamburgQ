from django.contrib import admin

from .models import Quiz,Question,Choice,WaitingRoom

admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Choice)
admin.site.register(WaitingRoom)