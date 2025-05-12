from django.shortcuts import render, get_object_or_404
from . import models

def films_list_view(request):
    if request.method == 'GET':
        film = models.Films.objects.all().order_by('-id')
        context = {
            'film': film,
        }
        return render(request,
                    template_name='films/films.html',
                    context=context
                    )

# получение id и вывод detail
def film_detail_view(request, id):
    if request.method == 'GET':
        film_id = get_object_or_404(models.Films, id=id)
        context = {
            'film_id': film_id,
        }
        return render(request, 
                    template_name='films/film_detail.html',
                    context=context
                    )