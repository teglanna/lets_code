from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def home(request):
    return render(request, 'blog/home.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def python(request):
	return render(request, 'blog/python.html', {})

def javascript(request):
	return render(request, 'blog/javascript.html')

def learning_stuffs(request):
	return render(request, 'blog/learning_stuffs.html')

def balls(request):
	return render(request, 'blog/balls.html')

def horse(request):
	return render(request, 'blog/horse.html')

def finefinder(request):
	return render(request, 'blog/finefinder.html')

def learning_stuffs(request):
	return render(request, 'blog/learning_stuffs.html')