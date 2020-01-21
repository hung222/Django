from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.StackedInline):
    model = Comment
class PostAdmin(admin.ModelAdmin):
    list_display  = ['title', 'date']
    list_filter   = ['date']
    search_fields = ['title']
    inlines       = [CommentInline] 
    # search_fields = ['id']
admin.site.register(Post, PostAdmin)

