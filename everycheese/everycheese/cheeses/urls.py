from django.urls import path

from . import views


app_name = 'cheeses'

urlpatterns = [
    path(
        route='',
        view=views.CheeseListView.as_view(),
        name='list',
    ),
    path(
        route='creer/',
        view=views.CheeseCreateView.as_view(),
        name='add',
    ),
    path(
        route='<slug:slug>/modifier/',
        view=views.CheeseUpdateView.as_view(),
        name='update',
    ),
    path(
        route='<slug:slug>/',
        view=views.CheeseDetailView.as_view(),
        name='detail',
    ),
]