from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.form import PostCreateForm
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

def post_create(request):
    if request.method =='GET':
        form = PostCreateForm()
        context = {
            'form' : form,

        }
        return render(request, 'blog/post_create.html',context=context)
    elif request.method =='POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():


            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            user = User.objects.first()
            post = Post.objects.create(
                title = title,
                text=text,
                author=user,
            )
            #return HttpResponse(post)
            return redirect('post_detail', pk=post.pk)
        else:
            context = {
                'form' : form,
            }
            return render(request)

def post_modify(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        data = request.POST
        title = data['title']
        text = data['text']
        post.title = title
        post.text = text
        post.save()
        return redirect('post_detail', pk=post.pk)
    elif request.method =='GET':
        context = {
            'post' : post,
        }
        return render(request, 'blog/post_modify.html', context=context)