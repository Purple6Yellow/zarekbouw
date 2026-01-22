from django.contrib import admin
from .models import *

@admin.register(Portfolio)
class Portfolio(admin.ModelAdmin):
    list_display =("naam",)
    list_filter = ("naam",)
