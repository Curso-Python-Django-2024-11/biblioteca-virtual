from django.urls import include, path
from bookshelf.views import LibroListView, LibroView, LibroViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'libros', LibroViewSet)


urlpatterns = [
    path('', LibroListView.as_view(), name='libro_list'),
    path('<int:pk>', LibroView.as_view(), name='libro_detail'),
    path('api/', include(router.urls)),
]
