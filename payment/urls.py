from django.urls import path
from .views import product_view, payment_view, success_view

app_name = 'payment'

urlpatterns = [
    path('', product_view, name='product'),
    path('payment/<int:pk>/', payment_view, name='payment'),
    path('success/', success_view, name='success'),

]
