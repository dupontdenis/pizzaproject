from django.urls import path
from .views import PizzaListApi, PizzaDetailByNameApi

urlpatterns = [
    path('pizzas/', PizzaListApi.as_view()),
    path('pizzas/<str:name>/', PizzaDetailByNameApi.as_view()),
]