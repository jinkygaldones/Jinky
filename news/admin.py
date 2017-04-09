from django.contrib import admin

# Register your models here.
from .models import News

class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated', 'timestamp', 'user']
    list_display_links = ["updated"]
    list_filter = ['updated', 'timestamp']
    search_fields = ['title', 'content']
    class Meta:
        model = News
admin.site.register(News, NewsModelAdmin)