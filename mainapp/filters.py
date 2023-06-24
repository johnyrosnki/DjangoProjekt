import django_filters

from .models import *


class IncomesFilter(django_filters.FilterSet):
    class Meta:
        model = Incomes
        fields = '__all__'


class ExpensesFilter(django_filters.FilterSet):
    class Meta:
        model = Expenses
        fields = '__all__'
