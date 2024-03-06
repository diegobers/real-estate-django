import django_filters

from .models import Casa


class CasaFilter(django_filters.FilterSet):
    class Meta:
        model = Casa
        fields = ["id", "category", "city", "price"]

class ListCasaFilter(django_filters.FilterSet):
    class Meta:
        model = Casa
        fields = ["category", "city", "price"]
