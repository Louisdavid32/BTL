from django.shortcuts import render
from btlgd.models import Article, Call

# Create your views here.


def index(request):
    articles = Article.objects.all()
    return render(request, 'page/index.html', context={'articles': articles})


def product(request):
    articles = Article.objects.all()
    return render(request, 'page/products.html', context={'articles': articles})


def description(request):
    articles = Call.objects.all()
    return render(request, 'page/des.html', context={'articles': articles})


def contact(request):
    articles = Call.objects.all()
    return render(request, 'page/contact.html', context={'articles': articles})