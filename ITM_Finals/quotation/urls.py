from django.urls import path
from . import views

app_name = 'quotation'

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('<int:id>/my_orders_items/',views.my_orders_items, name='my_orders_items'),
    path('process_order/', views.process_order, name='process_order'),
]