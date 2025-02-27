from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('<str:pk>', views.app, name = "app_with_pk"),
]