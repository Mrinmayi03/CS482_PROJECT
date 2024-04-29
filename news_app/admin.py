from django.contrib import admin

from .models import NewsVideo

@admin.register(NewsVideo)
class NewsVideoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "duration", "youtube_link", "is_summarized", "summary")

    
    
    