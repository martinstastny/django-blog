from django.contrib import admin
from .models import Post, Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("name",)}

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'user', 'created_at', 'updated_at')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)