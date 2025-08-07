from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(UserRecord)
class UserRecordAdmin(admin.ModelAdmin):
    pass