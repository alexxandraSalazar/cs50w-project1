from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entryPage, name="entryPage"),
    path("wiki/", views.search, name="search"),
    path('wiki/random/', views.randomm, name='random'),
    path("wiki/newPage/", views.newPage, name="newPage"),
    path('wiki/edit/', views.edit, name='edit'),
    path('wiki/save/', views.save, name='save'),
]
