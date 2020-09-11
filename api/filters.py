from django.db.models import Q
from django_filters import rest_framework as filters
from .models import Follow


class FollowFilter(filters.FilterSet):
    search = filters.CharFilter(method='filter_with_or')

    class Meta:
        model = Follow
        fields = ['search', ]

    def filter_with_or(self, queryset, name, value):
        return queryset.filter(
            Q(user__username=value) | Q(following__username=value)
        )
