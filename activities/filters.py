import django_filters
from .models import Activity

class ActivityFilter(django_filters.FilterSet):
    date_from = django_filters.DateFilter(field_name="date", lookup_expr="gte")
    date_to = django_filters.DateFilter(field_name="date", lookup_expr="lte")
    activity_type = django_filters.CharFilter(field_name="type", lookup_expr="iexact")
    min_duration = django_filters.NumberFilter(field_name="duration_minutes", lookup_expr="gte")
    max_duration = django_filters.NumberFilter(field_name="duration_minutes", lookup_expr="lte")

    class Meta:
        model = Activity
        fields = ["activity_type"]

