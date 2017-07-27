from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import BlogForm
from django.template.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth


def blog_list(request):
    blogs = Blog.objects.filter(blog_published_date__lte=timezone.now()).order_by('blog_published_date')
    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})


def blog_new(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.blog_author = request.user
            blog.blog_published_date = timezone.now()
            blog.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm()
    return render(request, 'blog_edit.html', {'form': form})


def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.blog_author = request.user
            blog.blog_published_date = timezone.now()
            blog.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog_edit.html', {'form': form})


def subscribe(request):
    if request.method == "POST":
            blog = Blog(subscribe=request.POST.get("subscribe", ""), blog_author=request.user)
            blog.save()

            return redirect('/blog_list/')


def home(request):
    context = {}
    template = "home.html"
    return render(request, template, context)


@login_required()
def userProfile(request):
    user = request.user
    context = {'user': user}
    template = "profile.html"
    return render(request, template, context)