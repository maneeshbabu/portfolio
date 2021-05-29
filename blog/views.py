from django.shortcuts import render, get_object_or_404

from .models import Blog

# Create your views here.

def index(request):
    blogs = Blog.objects.order_by('-created_at')[:5]
    return render(request, 'blogs/index.html', {'blogs': blogs})


def show(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/show.html', {'blog': blog})
    