
from django.urls import path
from . views import rubriques

urlpatterns = [

    path('', rubriques, name='rubriques' )]
  