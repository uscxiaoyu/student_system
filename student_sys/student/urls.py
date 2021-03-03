from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("downloadDocx", views.DownloadDocxView.as_view(), name="main")
]
