from django.urls import path

from .import views


urlpatterns = [
    path('search', views.search_stock, name = 'search_stock'),
    path('',views.index, name = "index")
   
]
