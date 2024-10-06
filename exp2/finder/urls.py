from django.urls import path
from . import views

urlpatterns = [
    path('odd-even/', views.odd_even_checker, name='odd_even_checker'),
    path('name-filter/', views.name_filter, name='name_filter'),
]
