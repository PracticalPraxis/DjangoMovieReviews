from django.shortcuts import render
from .models import NewsObject

def news(request):
    newsObjects = NewsObject.objects.all().order_by('-date')
    return render(request, 'news.html', {'newsObjects':newsObjects})
