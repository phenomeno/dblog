from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from markdown2 import markdown
from .models import Post


def detail(request, post_id, slug=None):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/detail.html', {'post': post})

def index(request):
    return render(request, 'posts/about.html', {})

def projects(request):
    latest_projects_list = Post.objects.filter(post_category='project').order_by('-written_date')
    for project in latest_projects_list:
        project.post_body = markdown(project.post_body)
    p = Paginator(latest_projects_list, 5)
    page = p.page(int(request.GET.get('page', '1')))
    context = {
        'paginated_list': page
    }
    return render(request, 'posts/projects.html', context)

def blog(request):
    latest_posts_list = Post.objects.filter(post_category='blog').order_by('-written_date')
    for post in latest_posts_list:
        post.post_body = markdown(post.post_body)
    p = Paginator(latest_posts_list, 5)
    page = p.page(int(request.GET.get('page', '1')))
    context = {
        'paginated_list': page
    }
    return render(request, 'posts/blog.html', context)
