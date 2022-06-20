import django_filters
from .models import Command


class CommandFilter(django_filters.FilterSet):
    class Meta:
        model = Command
        fields = ['product', 'statut']

