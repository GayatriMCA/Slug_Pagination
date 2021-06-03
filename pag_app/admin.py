from django.contrib import admin
from .models import Blog_Website

class WebsiteAdmin(admin.ModelAdmin):
    #list_display = ['Title']
    prepopulated_fields = {
        'slug' : ('Title',)
    }

admin.site.register(Blog_Website, WebsiteAdmin)