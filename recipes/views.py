from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import F
from . import models, forms

#create
class CreateRecipeView(generic.CreateView):
    template_name = 'recipes/recipe_form.html'
    form_class = forms.RecipeForm
    success_url = '/recipes/'
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

#read
class RecipeListView(generic.ListView):
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'
    model = models.Recipe
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')




#update
class RecipeUpdateView(generic.UpdateView):
    template_name = 'recipes/recipe_update.html'
    form_class = forms.RecipeForm
    success_url = '/recipes/'

    def get_object(self, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(models.Recipe, id=recipe_id)
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

#delete
class RecipeDeleteView(generic.DeleteView):
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = '/recipes/'

    def get_object(self, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(models.Recipe, id=recipe_id)

#search
class RecipeSearchView(generic.ListView):
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'
    model = models.Recipe
    def get_queryset(self):
        return self.model.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
    
#detail
class RecipeDetailView(generic.DetailView):
    model = models.Recipe
    template_name = 'recipes/recipe_detail.html'
    def get_object(self, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(models.Recipe, id=recipe_id)

class CreateIngredientView(generic.CreateView):
    model = models.Ingredient
    form_class = forms.IngredientForm
    template_name = 'recipes/ingredient_form.html'

    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'id': self.kwargs['recipe_id']})
    def form_valid(self, form):
        recipe = get_object_or_404(models.Recipe, id=self.kwargs['recipe_id'])
        form.instance.recipe = recipe
        return super().form_valid(form)
    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_id'] = self.kwargs['recipe_id']
        return context

class UpdateIngredientView(generic.UpdateView):
    model = models.Ingredient
    form_class = forms.IngredientForm
    template_name = 'recipes/ingredient_form.html'
    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'id': self.object.recipe.id})
    def get_object(self, **kwargs):
        ingredient_id = self.kwargs.get('id')
        return get_object_or_404(models.Ingredient, id=ingredient_id)

class DeleteIngredientView(generic.DeleteView):
    model = models.Ingredient
    template_name = 'recipes/ingredient_confirm_delete.html'
    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'id': self.object.recipe.id})
    def get_object(self, **kwargs):
        ingredient_id = self.kwargs.get('id')
        return get_object_or_404(models.Ingredient, id=ingredient_id)