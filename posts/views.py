from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

import ast
from markdown2 import markdown
from .models import Post


def detail(request, post_id, slug=None):
    post = get_object_or_404(Post, pk=post_id)
    split_body = post.post_body.split("]", 1)
    split_body = [n.strip() for n in split_body]
    if len(split_body) > 1:
        img_list = ast.literal_eval(split_body[0]+"]")
        post.post_body = markdown(split_body[1])
    else:
        img_list = []
        post.post_body = markdown(split_body[0])
    post.image_urls = img_list
    return render(request, 'posts/detail.html', {'post': post})

def index(request):
    return render(request, 'posts/about.html', {})

def projects(request):
    latest_projects_list = Post.objects.filter(post_category='project').order_by('-written_date')
    for project in latest_projects_list:
        split_body = project.post_body.split("]", 1)
        split_body = [n.strip() for n in split_body]
        if len(split_body) > 1:
            img_list = ast.literal_eval(split_body[0]+"]")
            project.post_body = markdown(split_body[1])
        else:
            img_list = []
            project.post_body = markdown(split_body[0])
        print project.post_body
        project.image_urls = img_list
    p = Paginator(latest_projects_list, 5)
    page = p.page(int(request.GET.get('page', '1')))
    context = {
        'paginated_list': page,
    }
    return render(request, 'posts/projects.html', context)

def blog(request):
    latest_posts_list = Post.objects.filter(post_category='blog').order_by('-written_date')
    for post in latest_posts_list:
        split_body = post.post_body.split("]", 1)
        split_body = [n.strip() for n in split_body]
        if len(split_body) > 1:
            img_list = ast.literal_eval(split_body[0]+"]")
            post.post_body = markdown(split_body[1])
        else:
            img_list = []
            post.post_body = markdown(split_body[0])
        post.image_urls = img_list
    p = Paginator(latest_posts_list, 5)
    page = p.page(int(request.GET.get('page', '1')))
    context = {
        'paginated_list': page
    }
    return render(request, 'posts/blog.html', context)
