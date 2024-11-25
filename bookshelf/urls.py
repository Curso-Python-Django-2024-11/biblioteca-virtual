from django.urls import path
from bookshelf.views import LibroListView, LibroView

urlpatterns = [
    path('', LibroListView.as_view(), name='libro_list'),
    path('<int:pk>', LibroView.as_view(), name='libro_detail'),
]
