from ..models import Post
from django import template

register = template.Library()

# 注册模板标签 可以使用{%get_recent_posts%}


@register.simple_tag()
def get_recent_posts(num=3):
    return Post.objects.all().order_by('article_id')[num:]

