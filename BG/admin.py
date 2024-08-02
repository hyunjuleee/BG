from django.contrib import admin
from .models import Q, Comment

# Register your models here.
admin.site.register(Q)
admin.site.register(Comment)