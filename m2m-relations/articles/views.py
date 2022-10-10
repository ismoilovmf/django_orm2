from django.shortcuts import render
from .models import Article

def articles_list(request):
    print(object_list:=Article.objects.all())
    template = 'articles/news.html'
    context = {'object_list': object_list}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    return render(request, template, context)
