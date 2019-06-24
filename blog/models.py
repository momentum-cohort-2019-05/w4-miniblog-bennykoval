from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class BlogAuthor(models.Model):
    """
    Blogger model
    """
    blogger_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    biography = models.TextField(max_length=400, help_text='Please write a biography no longer than 400 characters.')

    class Meta:
        ordering = ['user', 'biography']

    def get_absolute_url(self):
        """Returns the url to access a specific blog author instance"""
        return reverse('blogger-detail', args=[str(self.id)])

    def __str__(self):
        """String representing the blogger username"""
        return f'{self.blogger_name}'


# blogger_user_name = BlogAuthor.blogger_name

class BlogPost(models.Model):
    """
    Blog post model
    """
    blog_post_title = models.CharField(max_length=200)
    blogger = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=2000, help_text="Write your blog text here.")
    timestamp = models.DateField(default=date.today)
    # blogger_user_name = BlogAuthor.blogger_name

    # def display_blogger(self):
    #     """Create a string for the Blogger. This is required to display blogger in Admin."""
    #     return self.blogger_user_name
    
    # display_blogger.short_description = 'Blogger'

    class Meta:
        ordering = ['-timestamp']

    def get_absolute_url(self):
        """
        Returns the url to access a particular blog instance.
        """
        return reverse('blog_detail', args=[str(self.id)])

    def __str__(self):
        """String to represent the blog post object"""
        return self.blog_post_title

class BlogComment(models.Model):
    """Model representing a comment on a post"""
    comment_field = models.TextField(max_length=1000, help_text="Write your commentary here.")
    commentor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        """String representing the model object"""
        char_limit=75
        
        if len(self.comment_field) > char_limit:
            title_string = self.comment_field[:char_limit] + '...'
        else:
            title_string = self.comment_field
        return title_string

# class Question(models.Model):
#     text = models.TextField()
#     # ...

# class Answer(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     # ...

#     class Meta:
#         order_with_respect_to = 'question'