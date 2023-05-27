from django.views.generic import DetailView, ListView

from .filters import OrderFilter
from .models import *

# Create your views here.


class OrdersHomepage(ListView):
    model = WorkingOrder
    template_name = 'Order/homepage.html'
    ordering = '-creation_date'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = WorkingOrder.objects.all().order_by(self.ordering)
        queryset = OrderFilter(self.request.GET, queryset=queryset).qs
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = OrderFilter(self.request.GET)
        return context


class OrderDetailView(DetailView):
    model = WorkingOrder
    template_name = 'Order/detail.html'
    context_object_name = 'order'
