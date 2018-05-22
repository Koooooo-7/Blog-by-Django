from django.shortcuts import render, get_object_or_404
from comments.forms import CommentForm
import markdown
# Create your views here.
from .models import Post


def index(request):
    post_list = Post.objects.all().order_by('article_id')
    return render(request, 'index.html', context={'post_list': post_list})


def detail(request, get_id):
    # print("GET_ID:", get_id)
    post = get_object_or_404(Post, pk=get_id)
    post.text = markdown.markdown(post.text)

    form = CommentForm()
    comment_list = post.comment_set.all()

    contexts = {
        'post': post,
        'form': form,
        'comment_list': comment_list,
    }
    return render(request, 'detail.html', context=contexts)




