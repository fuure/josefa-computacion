from django.urls import path
from .views import (
    CustomerListView, CustomerDetailView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView,
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    PurchaseListView, PurchaseDetailView, PurchaseCreateView, PurchaseUpdateView, PurchaseDeleteView,
)

urlpatterns = [
    # URLs para Customer
    path('customer_list/', CustomerListView.as_view(), name='customer_list'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customer/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customer/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customer/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),

    # URLs para Product
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    # URLs para Purchase
    path('purchase_list/', PurchaseListView.as_view(), name='purchase_list'),
    path('purchase/<int:pk>/', PurchaseDetailView.as_view(), name='purchase_detail'),
    path('purchase/create/', PurchaseCreateView.as_view(), name='purchase_create'),
    path('purchase/<int:pk>/update/', PurchaseUpdateView.as_view(), name='purchase_update'),
    path('purchase/<int:pk>/delete/', PurchaseDeleteView.as_view(), name='purchase_delete'),
]
