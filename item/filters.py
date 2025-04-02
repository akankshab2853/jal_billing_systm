import django_filters
from .models import Stock

class StockFilter(django_filters.FilterSet):
    stock_type = django_filters.ChoiceFilter(field_name='stock_type', choices=Stock.STOCK_TYPE_CHOICES)

    class Meta:
        model = Stock
        fields = ["stock_type"]
