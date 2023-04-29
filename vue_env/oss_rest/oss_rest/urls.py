from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from portfolio import views

urlpatterns = [
    path('', views.inventory_list),
    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token),

    # Customer Endpoints
    path('customers/', views.customer_list),
    url(r'^api/customers/$', views.customer_list),
    url(r'^api/customers/(?P<pk>[0-9]+)/$', views.customer_detail),

    # Inventory Endpoints
    path('inventories/', views.inventory_list),
    url(r'^api/inventories/$', views.inventory_list),
    url(r'^api/inventories/(?P<pk>[0-9]+)/$', views.inventory_detail),

    # Order Endpoints
    path('orders/', views.order_list),
    url(r'^api/orders/$', views.order_list),
    url(r'^api/orders/(?P<pk>[0-9]+)/$', views.order_detail),

    path('register/', views.RegisterView, name='auth_register'),
]

