from django.shortcuts import render


def pageNotFound(request):
    return render(request, 'server/404.html')


def page_error(request):
    return render(request, 'server/500.html')


def about(request):
    return render(request, 'server/about.html')
