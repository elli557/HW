from django.urls import path
from . import views

urlpatterns = [
    path ('', views.FirstPageView.as_view(), name='index'),
]