from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'main_page' : 'Это главная страница проекта Yatube',
        'posts' : posts
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    template = 'posts/group_list.html'
    context = {
        'main_page': 'Здесь будет информация о группах проекта Yatube',
        'group': group,
        'posts': posts
    }
    return render(request, template, context)
   
