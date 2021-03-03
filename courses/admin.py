from django.contrib import admin
from .models import Course,Category,Level,Teacher
# Register your models here.
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Level)
admin.site.register(Teacher)