from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("add_listing", views.add_listing, name="add_listing"),
    path("register", views.register, name="register")
]
