from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template = 'posts/index.html'
    context = {
        'main_page' : 'Это главная страница проекта Yatube'
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    context = {
        'main_page': 'Здесь будет информация о группах проекта Yatube'
    }
    return render(request, template, context)
    #HttpResponse('Список posts')


#def group_posts(request, slug):
    return HttpResponse('Список posts')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
#def ice_cream_detail(request, pk):
#    return HttpResponse(f'Мороженое номер {pk}')