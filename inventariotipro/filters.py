import django_filters
from .models import Asignacion


class AsignacionFilter(django_filters.FilterSet):
    class Meta:
        model = Asignacion
        fields = '__all__'