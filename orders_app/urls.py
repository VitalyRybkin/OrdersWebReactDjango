from django.urls import path

from orders_app import views

app_name = "orders_app"

urlpatterns = [
    path("", views.index, name="index"),
]
