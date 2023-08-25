from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    # Get the list of posts
    posts = Post.published.all()
    return render(request, 
                  'blog/post/list.html',
                  {'posts': posts})


def post_detail(request, year, month, day, post):
    # Get the details of a post by its id
    post = get_object_or_404(Post, 
                             status=Post.Status.PUBLISHED, 
                             slug=post, 
                             publish__year=year, 
                             publish__month=month, 
                             publish__day=day)
    
    return render(request, 
                  'blog/post/detail.html',
                  {'post': post})
    
