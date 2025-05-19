from django.urls import path
from . import views

urlpatterns = [
    path ('film_list/', views.FilmsListView.as_view(), name='film_list'),
    path('film_list/<int:id>/', views.FilmsDetailView.as_view(), name='film_detail'),
    path ('film_list/<int:id>/delete/', views.DeleteFilmsView.as_view(), name='delete_film'),
    path ('film_list/<int:id>/update/', views.UpdateFilmsView.as_view(), name='update_film'),
    path ('create_film/', views.CreateFilmsView.as_view(), name='create_film'),
    path ('search/', views.SearchFilmsView.as_view(), name='search'),

]