# Standard library imports
# (none in this case)

# Django imports
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Local app imports
from .models import Post
from .forms import PostForm


# ------------------ Post CRUD ------------------

@login_required
def post_list(request):
    search_query = request.GET.get('q', '')
    posts = Post.objects.filter(title__icontains=search_query) if search_query else Post.objects.all()

    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {
        "page_obj": page_obj,
        "search_query": search_query
    })


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)  # pre-fill form with post data

    return render(request, 'blog/post_form.html', {'form': form})



@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully!")
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})


# ------------------ Auth ------------------

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Post created bro!")
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})


# ------------------ Profile ------------------

@login_required
def profile_view(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/profile.html', {'user': request.user, 'posts': posts})
