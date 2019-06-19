from django.views import generic
from .models import Post
from django.shortcuts import render, redirect
from .models import Comment
from django.shortcuts import get_object_or_404
from .forms import CommentForm


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'news/index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'news/post_detail.html'


def add_comment_to_post(request):

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('post_detail')
    else:
        form = CommentForm()
    return render(request, 'news/post_detail.html', {'form': form})

