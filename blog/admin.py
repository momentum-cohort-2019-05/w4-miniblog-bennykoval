from django.contrib import admin

# Register your models here.

from blog.models import BlogAuthor, BlogPost, BlogComment

# admin.site.register(BlogAuthor)
# admin.site.register(BlogPost)
# admin.site.register(BlogComment)

# Register the Admin classes for Book using the decorator
@admin.register(BlogAuthor)
class BlogAuthorAdmin(admin.ModelAdmin):
    list_display = ('blogger_name', 'biography')

# Register the Admin classes for BookInstance using the decorator
@admin.register(BlogPost) 
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('blog_post_title', 'timestamp', 'blogger')

@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    pass