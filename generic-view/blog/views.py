from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    queryset            = Post.objects.all().order_by("-date")
    template_name       = 'blog/blog.html'
    context_object_name = 'Posts'
    paginate_by         = 2

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
