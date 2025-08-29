from orders_app import views
from django.urls import path

app_name = "orders_app"

urlpatterns = [
    path("", views.index, name="index"),
]
