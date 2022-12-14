from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    objects = Article.objects.all().order_by(ordering)
    context = {'object_list': objects}
    return render(request, template, context)
