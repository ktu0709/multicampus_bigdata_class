from django.urls import path

from . import views

urlpatterns = [
    path("myfor/", views.myfor, name="myfor"),
    path("myexam/", views.myexam, name="myexam"),
    path("01/", views.index, name="index"),
    path("02/", views.index02, name="index02"),
    path("render/", views.my_render_view, name="my_render_view"),
    path("redirect/", views.my_redirect_view, name="my_redirect_view"),
    path("json/", views.my_json, name="my_json"),

    #tutorial
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]