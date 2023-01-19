from django.urls import path
from . import views
from .views import addition, subtract, remove, create_cartitem

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('home/', views.home, name="home"),
    path('checkout/', views.checkout, name="checkout"),
    path('profile/', views.profile, name="profile"),

    path('create_cartitem/<str:pk>', create_cartitem, name="create_cartitem"),
    path('add/<str:id>', addition, name="addition"),
    path('subtract/<str:id>', subtract, name="subtract"),
    path('remove/<str:id>', remove, name="remove"),

    path('authorization/', views.authorization, name="authorization"),
]
