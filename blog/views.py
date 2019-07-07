from django.contrib.auth.decorators import login_required
from blog.forms import PostCreateForm, CommentForm
from django.shortcuts import render, redirect, get_object_or_404

from .models import Post, Comment


@login_required
def home(request):
    posts = Post.objects.all()
    data = dict()
    data['posts'] = posts
    return render(request, 'home.html', data)


@login_required
def list_post(request):
    template_name = 'blog/post_list.html'
    posts = Post.objects.filter(created_by=request.user)
    data = {}
    data['posts'] = posts
    return render(request, template_name, data)


@login_required
def view_post(request, pk):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.instance.post = post
        form.instance.commented_by = request.user
        form.save()
        return redirect('view_post', pk=pk)
    comments = Comment.objects.filter(post=post)
    return render(request, template_name, {'post': post, 'form': form, 'comments': comments})


@login_required
def create_post(request):
    template_name = 'blog/post_form.html'
    form = PostCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.created_by = request.user
        form.save()
        return redirect('list_post')
    return render(request, template_name, {'form': form})


@login_required
def edit_post(request, pk):
    template_name = 'blog/post_form.html'
    post = get_object_or_404(Post, pk=pk)
    form = PostCreateForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('list_post')
    return render(request, template_name, {'form': form})


@login_required
def delete_post(request, pk):
    template_name = 'blog/post_confirm_delete.html'
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('list_post')
    return render(request, template_name, {'object': post})
