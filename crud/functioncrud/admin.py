from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass
