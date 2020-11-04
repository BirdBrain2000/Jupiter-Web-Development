from django.urls import path

from . import views

urlpatterns = [
    path('jupiter/', views.jupiter, name='jupiter'),
    path('jupiter/delete/<list_id>', views.delete, name='delete'),
    path('jupiter/cross_off/<list_id>', views.cross_off, name='cross_off'),
    path('jupiter/uncross/<list_id>', views.uncross, name='uncross'),
    ]