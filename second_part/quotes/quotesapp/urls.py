from django.urls import path
from . import views


app_name = 'quotesapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('quote/', views.create_quote, name='create_quote'),
    path('tag/', views.tag, name='tag'),
    path('quotes/', views.quotes_view, name='quotes'),
    path('authors/', views.authors, name='authors'),
    path('author/create/', views.create_author, name='create_author'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
]
