from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect

class PostListView(ListView):
    queryset            = Post.objects.all().order_by("-date")
    template_name       = 'blog/blog.html'
    context_object_name = 'Posts'
    paginate_by         = 2

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
# User access url and send request -> view and process (library, function, model) -> render data and template
def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        # Must be login to comment
        # request.POST, author=request.user, post=post be stored in *args and **kwargs variables
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
    return render(request, "blog/post.html", {'post':post, 'form':form})