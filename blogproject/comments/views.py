from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm

# Create your views here.
"""
首先我们使用了 redirect 函数。这个函数位于 django.shortcuts 模块中，
它的作用是对 HTTP 请求进行重定向（即用户访问的是某个 URL，但由于某些原因，
服务器会将用户重定向到另外的 URL）。redirect 既可以接收一个 URL 作为参数，
也可以接收一个模型的实例作为参数（例如这里的 post）。如果接收一个模型的实例，
那么这个实例必须实现了 get_absolute_url 方法，这样 redirect 
会根据 get_absolute_url 方法返回的 URL 值进行重定向。
"""


def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    # 获取POST表单数据 -> dict
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            print("VALID")
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            print("NOT VALID")
            comment_list = post.comment_set.all()
            context = {
                'post': post,
                'form': form,
                'comment_list': comment_list
            }
            return render(request, 'detail.html', context=context)
    return redirect(post)
