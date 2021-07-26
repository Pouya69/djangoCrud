from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello),
    path('operations', views.operations),
    path('result', views.result),
    path('createOrder', views.create_order),
    path('createUser', views.create_user),
    path('updateOrder/<int:pk>', views.update_order, name="update_order"),
    path('deleteOrder/<int:pk>', views.delete_order, name="delete_order"),
    path('', views.dashboard, name="dashboard"),
]
