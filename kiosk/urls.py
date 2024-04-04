from django.urls import path

from . import views

app_name = "kiosk"
urlpatterns = [
    # path("", views.home, name="home"),
    path("", views.CategoryListView.as_view(), name='index'),
    path("kiosk/<int:pk>/", views.MenuDetailView.as_view(), name="detail")
]
