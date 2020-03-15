
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contestants', views.contestants, name='contestants'),
    path('<int:contestant_id>/vote', views.vote, name='vote')
]
