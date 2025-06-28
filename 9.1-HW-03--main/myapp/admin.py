from django.contrib import admin
from .models import Author, Category, Post, Comment, PostCategory

class PostCategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1  

class PostAdmin(admin.ModelAdmin):
    inlines = [PostCategoryInline]  
    list_display = ('title', 'author', 'post_type', 'created_at', 'display_categories')
    list_filter = ('post_type', 'categories', 'created_at')
    search_fields = ('title', 'text')
    
    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    display_categories.short_description = 'Категории'

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
