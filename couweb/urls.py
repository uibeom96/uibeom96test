from django.urls import path
from couweb import views


app_name = "webs"

urlpatterns = [
    path('', views.get_url, name="main"),
    path('<str:slug>/', views.get_url, name="current_main"),
]


