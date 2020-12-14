
from django.contrib import admin
from django.urls import path, include
from projeto_lista import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projeto_lista.urls')),
]
