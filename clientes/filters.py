from django_filters.rest_framework import BaseInFilter, FilterSet

from clientes.models import Cliente

class _NumberInFilter(BaseInFilter):
    pass

class ClienteFilters(FilterSet):
    id__in = _NumberInFilter(field_name='id', lookup_expr='in')
    
    class Meta:
        model = Cliente
        fields = '__all__'