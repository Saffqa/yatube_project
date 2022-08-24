from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Добрый день! Вы находитесь на главной странице новой социальной'
                        'сети "Yatube"')

def group_posts(request, slug):
    return HttpResponse(f'Перед Вами представлен список постов, отсортированных по группам: {slug}')