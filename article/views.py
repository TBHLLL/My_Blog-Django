from django.shortcuts import render, redirect
from django.views import View

from .models import ArticlePost,ArticleColumn
from django.http import HttpResponse
from .forms import ArticlePostForm
from django.contrib.auth.models import User
import markdown
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q


def article_list(request):
    search = request.GET.get('search')
    order = request.GET.get('order')
    column = request.GET.get('column')
    tag = request.GET.get('tag')
    article_list = ArticlePost.objects.all()
    if search:
        article_list = ArticlePost.objects.filter(Q(title__icontains=search) | Q(body__icontains=search))
    else:
        search=''
    if column is not None and column.isdigit():
        article_list = article_list.filter(column=column)

    if tag and tag != 'None':
        article_list = article_list.filter(tags__name__in=[tag])
    if order == 'total_views':
        article_list = article_list.order_by('-total_views')

    paginator = Paginator(article_list, 20)
    # 获取 url 中的页码
    page = request.GET.get('page')
    # 将导航对象相应的页码内容返回给 articles
    articles = paginator.get_page(page)
    context = {'articles': articles, 'order': order, 'search': search, 'column': column, 'tag':tag }
    return render(request, 'article/list.html', context)


def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    article.total_views += 1
    article.save(update_fields=['total_views'])
    md = markdown.Markdown(
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc'
                                     ])
    article.body = md.convert(article.body)
    context = {'article': article,'toc': md.toc}
    return render(request, 'article/detail.html', context)


@login_required(login_url='/userprofile/login/')
def article_create(request):
    if request.method == "POST":
        article_post_form = ArticlePostForm(request.POST,request.FILES)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=request.user.id)
            if request.POST['column'] != 'none':
                new_article.column = ArticleColumn.objects.get(id=request.POST['column'])
            new_article.save()
            article_post_form.save_m2m()
            return redirect("article:article_list")
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    else:
        columns = ArticleColumn.objects.all()
        article_post_form = ArticlePostForm()
        context = {'article_post_form': article_post_form, 'columns': columns}
        return render(request, 'article/create.html', context)


@login_required(login_url='/userprofile/login/')
def article_safe_delete(request, id):
    if request.method == 'POST':
        article = ArticlePost.objects.get(id=id)
        if request.user != article.author:
            return HttpResponse("抱歉，你无权删除这篇文章。")
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("仅允许post请求")


@login_required(login_url='/userprofile/login/')
def article_update(request, id):
    """
        更新文章的视图函数
        通过POST方法提交表单，更新titile、body字段
        GET方法进入初始表单页面
        id： 文章的 id
    """
    article = ArticlePost.objects.get(id=id)
    if request.user != article.author:
        return HttpResponse("抱歉，你无权修改这篇文章。")
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            if request.POST['column'] != 'none':
                article.column = ArticleColumn.objects.get(id=request.POST['column'])
            else:
                article.column = None
            if request.FILES.get('avatar'):
                article.avatar = request.FILES.get('avatar')
            article.tags.set(*request.POST.get('tags').split(','),clear=True)
            article.save()
            return redirect("article:article_detail", id=id)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    else:
        columns = ArticleColumn.objects.all()
        article_post_form = ArticlePostForm()
        context = {'article': article, 'article_post_form': article_post_form,'columns': columns,}
        return render(request, 'article/update.html', context)

# 点赞数 +1
class IncreaseLikesView(View):
    def post(self, request, *args, **kwargs):
        article = ArticlePost.objects.get(id=kwargs.get('id'))
        article.likes += 1
        article.save()
        return HttpResponse('success')