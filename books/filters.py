from django_filters import rest_framework as filters


class BookFilter(filters.FilterSet):
    tags = filters.AllValuesMultipleFilter(
        field_name="tags__name",
        conjoined=True,
    )
    title = filters.CharFilter(field_name="title", lookup_expr="contains")
