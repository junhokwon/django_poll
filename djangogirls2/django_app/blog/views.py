from django.shortcuts import render
from blog.models import Post


def post_list(request):
    post = Post.objects.all()
    context = {
        'title' : '네이버 인기뉴스',
        'post' : post,

    }
    return render(request, 'blog/post_list.html',context=context)

def post_detail(request,pk):
    post = Post.objects.get(id=pk)
    context = {
        'post' : post,
    }
    return render(request,'blog/post_detail.html', context=context)