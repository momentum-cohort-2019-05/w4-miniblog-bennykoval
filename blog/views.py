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

class BlogPostListView(generic.ListView):
    model = BlogPost
    paginator = Paginator('BlogPost', 5)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BlogPostListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context = {'blog_post_title': 'blogger', 'description': 'timestamp'}
        context_object_name = 'posts_on_blog'
        return context

# def post_view(request):
#     num_posts = BlogPost.objects.all().count()
#     num_comments = BlogComment.objects.all().count()
        
#     num_bloggers = BlogAuthor.objects.count()
    
#     context = {
#         'num_posts': num_posts,
#         'num_comments': num_comments,
#         'num_bloggers': num_bloggers,
#     }
#     return render(request, 'blogpost_list.html', context=context)