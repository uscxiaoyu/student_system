from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("downloadDocx", views.downloadDocxView, name="downloadDocx"),
    path("checkDocx", views.checkDocxView, name="checkDocx"),
    path("logout", views.logoutView, name="logout")
]
