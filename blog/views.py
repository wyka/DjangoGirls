from django.shortcuts import render
from .models import Post

def post_list(request):
    lista=Post.objects.all()
    return render(request, 'blog/post_list.html', {'post': lista})
 
# Create your views here.
