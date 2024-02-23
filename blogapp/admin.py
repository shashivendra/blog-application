from django.contrib import admin
from .models import Category, Post, Author, Comment, Candidate


class CandidateAdmin(admin.ModelAdmin):
    list_display=('username', 'password', 'name', 'cnf_password')
    list_filter=('username', 'password', 'name')
    search_fields=('username', 'name')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    list_filter = ('name',)  
    search_fields = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'category', 'created_at', 'status')
    list_filter = ('title', 'author_name', 'category', 'status')  
    search_fields = ('title', 'author_name__author_name', 'category__name', 'content')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name',)
    search_fields = ('author_name',)
    list_filter = ('author_name',)  


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'message')
    search_fields = ('name', 'email', 'post__title', 'message')
    list_filter = ('post',) 

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Candidate, CandidateAdmin)
