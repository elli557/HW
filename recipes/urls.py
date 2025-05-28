from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.RecipeListView.as_view(), name='recipe_list'),
    path('create/', views.CreateRecipeView.as_view(), name='create_recipe'),
    path('recipes/<int:id>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/<int:id>/update/', views.RecipeUpdateView.as_view(), name='update_recipe'),
    path('recipes/<int:id>/delete/', views.RecipeDeleteView.as_view(), name='delete_recipe'),
    path('recipes/<int:recipe_id>/ingredients/create/', views.CreateIngredientView.as_view(), name='create_ingredient'),
    path('ingredients/<int:id>/update/', views.UpdateIngredientView.as_view(), name='update_ingredient'),
    path('ingredients/<int:id>/delete/', views.DeleteIngredientView.as_view(), name='delete_ingredient'),

    
]
