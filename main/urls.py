from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:id>", views.id_page, name="id_page"),
    path("create/", views.create, name="create"),
    path("lists/", views.lists, name="lists"),
]