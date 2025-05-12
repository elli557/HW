from django.urls import path
from . import views

urlpatterns = [
    path ('film_list/', views.films_list_view, name='film_list'),
    path('film_list/<int:id>/', views.film_detail_view, name='film_detail'),
    path ('film_list/<int:id>/delete/', views.delete_film_view, name='delete_film'),
    path ('film_list/<int:id>/update/', views.update_film_view, name='update_film'),
    path ('create_film/', views.create_film_view, name='create_film'),

]