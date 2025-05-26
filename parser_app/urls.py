from django.urls import path
from . import views


urlpatterns = [
    path('parser_form/', views.ParserForm.as_view(), name='parser_form'),
    path('kinob_list/', views.KinobListView.as_view(), name='kinob_list')
]