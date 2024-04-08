from django.urls import path

from . import views

app_name = "kiosk"
urlpatterns = [
    path("", views.home, name="home"),
    path("menu/<int:category_id>/", views.ProductLV.as_view(), name='category_list'),
    path("menu/", views.ProductLV.as_view(), name='menu_list'),
]
