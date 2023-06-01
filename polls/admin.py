from django.contrib import admin
from polls.models import People
from .models import Question

# Register your models here.

admin.site.register(People)
admin.site.register(Question)