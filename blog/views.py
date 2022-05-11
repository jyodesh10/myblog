from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from blog.forms import BlogForm
from django.contrib import messages

from blog.models import BlogModel

# Create your views here.


def home(request):
    blogs = BlogModel.objects.all()
    return render(request, 'blog/home.html', {'blogs': blogs})


def addBlog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data['title']
            form.cleaned_data['body']
            form.cleaned_data['img']
            form.save()
            HttpResponseRedirect('')
            if form is not None:
                messages.success(request, 'New Post Added Successfully!!')
                form = BlogForm()
                blogs = BlogModel.objects.all()
                return render(request, 'blog/home.html', {'blogs': blogs})
    else:
        form = BlogForm()
    return render(request, 'blog/addblog.html', {'form': form})


def updateBlog(request, id):
    if request.method == "POST":
        ob = BlogModel.objects.get(pk=id)
        form = BlogForm(request.POST, instance=ob)
        if form.is_valid():
            form.save()
            blogs = BlogModel.objects.all()
            return render(request, 'blog/home.html', {'blogs': blogs})
    else:
        ob = BlogModel.objects.get(pk=id)
        form = BlogForm(instance=ob)
    return render(request, 'blog/updateblog.html', {'form': form})


def deleteBlog(request, id):
    if request.method == "POST":
        ob = BlogModel.objects.get(pk=id)
        ob.delete()
        blogs = BlogModel.objects.all()
        return render(request, 'blog/home.html', {'blogs': blogs})
