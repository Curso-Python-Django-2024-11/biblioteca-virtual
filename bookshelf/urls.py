from django.urls import path
from bookshelf.views import LibroListView

urlpatterns = [
    path('', LibroListView.as_view(), name='libro_list'),
]
