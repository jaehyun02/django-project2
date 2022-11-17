from django.urls import path
from .views import *



urlpatterns = [
    path('', index),
    path('blog/',blog),
    path('blog/new_post/', new_post),
    path('blog/<int:pk>/remove/', remove_post),
]