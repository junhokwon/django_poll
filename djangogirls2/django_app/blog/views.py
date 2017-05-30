from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.models import Post


def post_list(request):
    post = Post.objects.order_by('-created date')
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

def post_create(request):
    if request.method =='GET':
        context = {

        }
        return render(request, 'blog/post_create.html',context=context)
    elif request.method =='POST':
        data = request.POST
        title = data['title']
        text = data['text']
        user = User.objects.first()
        post = Post.objects.create(
            title = title,
            text=text,
            author=user,
        )
        #return HttpResponse(post)
        return redirect('post_detail', pk=post.pk)