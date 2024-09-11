from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Post, Comment
from django.contrib.auth import login as auth_login
from .forms import RegisterForm, UserUpdateForm, CommentForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def showBlogList(request): 
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def showBlogDetails(request, id): 
    post = get_object_or_404(Post, pk=id)
    return render(request, 'details.html', {'post': post})

def blog_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog.html', context)

def register(request): 
    if request.method == 'POST': 
        form = RegisterForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    
    else: 
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})

def user_login(request): 
    if request.method == 'POST': 
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid(): 
            user = form.get_user()
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    
    else: 
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid(): 
            form.save()
            return redirect('profile')
    
    else: 
        form = UserUpdateForm(instance=request.user)

    return render(request, 'profile.html', {'form': form})

@login_required
def add_comment(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST': 
        form = CommentForm(request.POST)
        if form.is_valid(): 
            comment_content = form.cleaned_data['content']
            new_comment = {'author': request.user.username, 'content': comment_content} 
            post.comments.append(new_comment)
            post.save()
            return redirect('details', id=id)
        
    else: 
        form = CommentForm()
    
    return render(request, 'comment.html', {'form': form, 'post': post})

@login_required
def create_post(request): 
    if request.method == 'POST': 
        form = PostForm(request.POST)
        if form.is_valid(): 
            post = form.save(commit=False)
            post.author = request.user.username
            post.save()
            return redirect('bloglist')
    
    else: 
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})


@login_required
def edit_post(request, id): 
    post = get_object_or_404(Post, pk=id)
    if post.author != request.user.username: 
        return HttpResponse("You don't have permission to edit this post.")
    
    if request.method == 'POST': 
        form = PostForm(request.POST, instance=post)
        if form.is_valid(): 
            form.save()
            return redirect('details', id=id)
    
    else: 
        form = PostForm(instance=post)
    
    return render(request, 'edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, id): 
    post = get_object_or_404(Post, pk=id)
    if post.author != request.user.username: 
        return HttpResponse("You don't have permission to delete this post.")
    
    if request.method == 'POST':
        post.delete()
        return redirect('bloglist')
    

    return render(request, 'delete_post.html', {'post': post})