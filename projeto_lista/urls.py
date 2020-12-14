from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('delete/<list_id>', views.delete, name='delete'),
    path('check/<list_id>', views.check, name='check'),
    path('uncheck/<list_id>', views.uncheck, name='uncheck'),
    path('edit/<list_id>', views.edit, name='edit')
]
