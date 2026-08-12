from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("report/", views.report_trail, name="report_trail"),
    path("search/", views.search_trails, name="search_trails"),
]