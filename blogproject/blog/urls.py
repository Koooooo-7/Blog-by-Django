from django.conf.urls import url
from . import views
"""
    Django 使用正则表达式来匹配用户访问的网址。
    这里 r'^post/(?P<pk>[0-9]+)/$' 整个正则表达式刚好匹配
    我们上面定义的 URL 规则。这条正则表达式的含义是，以 post/ 开头，
    后跟一个至少一位数的数字，并且以 / 符号结尾，如 post/1/、 post/255/ 
    等都是符合规则的，[0-9]+ 表示一位或者多位数。
    此外这里 (?P<pk>[0-9]+) 表示命名捕获组，
    其作用是从用户访问的 URL 里把括号内匹配的字符串捕获
    并作为关键字参数传给其对应的视图函数 detail。
    比如当用户访问 post/255/ 时
    （注意 Django 并不关心域名，而只关心去掉域名后的相对 URL），
    被括起来的部分 (?P<pk>[0-9]+) 匹配 255，
    那么这个 255 会在调用视图函数 detail 时被传递进去，
    实际上视图函数的调用就是这个样子：detail(request, pk=255)。
    我们这里必须从 URL 里捕获文章的 id，因为只有这样我们才能知道用户访问的究竟是哪篇文章。
    """
app_name = 'blog'
urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^post/(?P<get_id>[0-9]+)/$', views.detail, name='detail')
]
