from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Category

class CommentItemInliene(admin.TabularInline):
    model = Comment
    raw_id_fields = ['Post']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title','intro','body']
    list_display =('title','category','created_at','status')
    list_filter = ['category','created_at','status']
    inlines = [CommentItemInliene]

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display =('title')

class CommentAdmin(admin.ModelAdmin):
    list_display =('name','post','created_at')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)