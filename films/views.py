from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.http import HttpResponse

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
    
# Create
def create_film_view(request):
    if request.method == 'POST':
        form = forms.FilmsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('film_list')
    else:
        form = forms.FilmsForm()
    return render(request, template_name='films/create_film.html', context={'form': form})

# Read
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
    
# Update
def update_film_view(request,id):
    film_id = get_object_or_404(models.Films, id=id)
    if request.method == "POST":
        form  = forms.FilmsForm(request.POST, instance=film_id)
        if form.is_valid():
            form.save()
            return redirect('film_list')
    else:
        form = forms.FilmsForm(instance=film_id)
    return render(request, template_name='films/update_film.html', context={
        'form': form,
        'film_id': film_id,
        })

# Delete
def delete_film_view(request, id):
    film_id = get_object_or_404(models.Films, id=id)
    film_id.delete()
    return redirect('film_list')