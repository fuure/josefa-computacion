from django.urls import path
from .views import index, create_item

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_item, name='create_item'),
]
