from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.http import HttpResponse
from django.views import generic
from django.db.models import F

# получение id и вывод detail
class FilmsDetailView(generic.DetailView):
    model = models.Films
    template_name = 'films/film_detail.html'
    pk_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        film = self.object
        viewed_films = request.session.get("viewed_films", [])
        if film.id not in viewed_films:
            film.views = F("views") + 1
            film.save()
            film.refresh_from_db()
            viewed_films.append(film.id)
            request.session["viewed_films"] = viewed_films
        return response

# def film_detail_view(request, id):
#     if request.method == 'GET':
#         film_id = get_object_or_404(models.Films, id=id)
#         context = {
#             'film_id': film_id,
#         }
#         return render(request, 
#                     template_name='films/film_detail.html',
#                     context=context
#                     )
    
# Create
class CreateFilmsView(generic.CreateView):
    template_name = 'films/create_films.html'
    form_class = forms.FilmsForm
    success_url = '/films_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateFilmsView, self).form_valid(form=form)

# def create_film_view(request):
#     if request.method == 'POST':
#         form = forms.FilmsForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('film_list')
#     else:
#         form = forms.FilmsForm()
#     return render(request, template_name='films/create_film.html', context={'form': form})


# Read
class FilmsListView(generic.ListView):
    template_name =  'films/films.html'
    context_object_name = 'film'
    model = models.Films

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
    
# def films_list_view(request):
#     if request.method == 'GET':
#         film = models.Films.objects.all().order_by('-id')
#         context = {
#             'film': film,
#         }
#         return render(request,
#                     template_name='films/films.html',
#                     context=context
#                     )
    
# Update
class UpdateFilmsView(generic.UpdateView):
    template_name = 'films/update_film.html'
    form_class = forms.FilmsForm
    success_url = '/film_list/'

    def get_object(self,  **kwargs):
        film_id = self.kwargs.get('id')
        return get_object_or_404(models.Films, id=film_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateFilmsView, self).form_valid(form=form)

# def update_film_view(request,id):
#     film_id = get_object_or_404(models.Films, id=id)
#     if request.method == "POST":
#         form  = forms.FilmsForm(request.POST, instance=film_id)
#         if form.is_valid():
#             form.save()
#             return redirect('film_list')
#     else:
#         form = forms.FilmsForm(instance=film_id)
#     return render(request, template_name='films/update_film.html', context={
#         'form': form,
#         'film_id': film_id,
#         })


# Delete
class DeleteFilmsView(generic.DeleteView):
    template_name = 'films/confirm_delete.html'
    success_url = '/films_list/'

    def get_object(self, **kwargs):
        film_id = self.kwargs.get('id')
        return get_object_or_404(models.Films, id=film_id)
# def delete_film_view(request, id):
#     film_id = get_object_or_404(models.Films, id=id)
#     film_id.delete()
#     return redirect('film_list')

#search
class SearchFilmsView(generic.ListView):
    template_name = 'films/films.html'
    context_object_name = 'film'
    paginate_by = 5
    model = models.Films

    def get_queryset(self):
        return self.model.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context