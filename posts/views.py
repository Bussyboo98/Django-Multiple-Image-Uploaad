from django.shortcuts import render, get_object_or_404 
from .models import *
 
def blog_view(request):
    blg_posts = Post.objects.all()
    return render(request, 'blog.html', {'blog':blg_posts})
 
def detail_view(request, id):
    blog_posts = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=blog_posts)
    return render(request, 'detail.html', { 'blogs':blog_posts,  'photos':photos })