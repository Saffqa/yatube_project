from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template = 'posts/index.html'
    return render(request, template)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    return render(request, template)
    #HttpResponse('Список posts')


#def group_posts(request, slug):
    return HttpResponse('Список posts')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
#def ice_cream_detail(request, pk):
#    return HttpResponse(f'Мороженое номер {pk}')