from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator
from blog.models import BlogPost, BlogComment, BlogAuthor

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_posts = BlogPost.objects.all().count()
    num_comments = BlogComment.objects.all().count()
    
    # Available books (status = 'a')
    
    # The 'all()' is implied by default.    
    num_bloggers = BlogAuthor.objects.count()
    
    context = {
        'num_posts': num_posts,
        'num_comments': num_comments,
        'num_bloggers': num_bloggers,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

# def BlogPostListView(request):
#     """View function for blog posts of site."""


class BlogPostListView(generic.ListView):
    model = BlogPost
    paginator = Paginator('BlogPost', 5)
