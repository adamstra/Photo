from django.urls import path
from .views import home, addPost

urlpatterns = [
    path('', home, name='home'),
    path('addpost/', addPost, name='addpost')
]
