from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

from .models import Post

def index(request):
    latest_post_list = Post.objects.order_by('-written_date')[:5]
    context = {
        'latest_post_list': latest_post_list,
    }
    return render(request, 'posts/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/detail.html', {'post': post})
