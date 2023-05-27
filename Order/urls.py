from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *


urlpatterns = [
    path('', OrdersHomepage.as_view(), name='orders_homepage'),
    path('<int:pk>', OrderDetailView.as_view(), name='order_detail'),
]
