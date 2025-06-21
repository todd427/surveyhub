from django.contrib import admin
from .models import Page  # Import your model(s)

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')  # Or whatever fields make sense
from django.contrib import admin

# Register your models here.
