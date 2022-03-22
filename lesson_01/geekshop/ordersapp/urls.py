import ordersapp.views as ordersapp
from django.urls import path

app_name="ordersapp"

urlpatterns = [
   path('', ordersapp.OrderList.as_view(), name='orders_list'),
   path('forming/complete/<int:pk>', ordersapp.order_forming_complete, name='order_forming_complete'),
   path('create/', ordersapp.OrderItemsCreate.as_view(), name='order_create'),
   path('read/<int:pk>/', ordersapp.OrderDetail.as_view(), name='order_read'),
   path('update/<int:pk>/', ordersapp.OrderUpdate.as_view(), name='order_update'),
   path('delete/<int:pk>/', ordersapp.OrderDelete.as_view(), name='order_delete'),
   path('product/<int:pk>/price/', ordersapp.product_price, name='product_price'),
]