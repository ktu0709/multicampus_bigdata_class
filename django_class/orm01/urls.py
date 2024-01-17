from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.index, name="orm01_index"),
    path("all/", views.address_list, name="address_list"),
    path("add/", views.address_add, name="address_add"),
]