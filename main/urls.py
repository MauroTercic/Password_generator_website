from django.urls import path
from . import views

urlpatterns = [path("", views.home, name="home"),
               path("home/", views.home, name="home"),
               path("create/", views.create, name="create"),
               path("show/", views.show_password, name="show_password"),
               path("samples/", views.samples, name="samples")
               ]