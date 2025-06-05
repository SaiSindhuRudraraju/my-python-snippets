from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('hello/', views.hello),
    path('SaveProduct/', views.SaveProduct, name='save_product'),
]
