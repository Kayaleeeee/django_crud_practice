from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post, Comment

# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detail', post.pk)

    else:
        form = PostForm()
        return render(request, 'new.html', {'form': form})


def detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', post.pk)
    else:
        form = CommentForm()

    return render(request, 'detail.html', {'post': post, 'form': form})


def edit(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detail', post.pk)

    else:
        form = PostForm(instance=post)
    return render(request, 'edit.html', {'form': form})


def delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post.delete()
    return redirect('home')


# ->>순서 사용자 요청(reqeust) ->상세 게시글(post_pk), 댓글 (comment_pk)
def delete_comment(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)


"""
이미지 파일 고정된 내용 불러올 땐 확장자까지 전부 포함해서 이미지 불러오기하면 된다!
<img src="{% static 'img/' %}" alt="">
"""
