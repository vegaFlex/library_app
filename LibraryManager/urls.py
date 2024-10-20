from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='catalog:book_list', permanent=True)),  # Пренасочване към списъка с книги
    path('', include('catalog.urls')),  # Включване на маршрутите от catalog
]

