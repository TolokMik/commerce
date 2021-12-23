from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("add_listing", views.add_listing, name="add_listing"),
    path("register", views.register, name="register"),
    path("staff_id/<str:staff_id>", views.staff_one, name="staff_id")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
