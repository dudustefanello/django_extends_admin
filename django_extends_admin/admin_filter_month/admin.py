from datetime import date as d

from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured
from django.template.defaultfilters import date
from django.utils.translation import gettext_lazy as _


class ListFilterMonth(admin.SimpleListFilter):
    lookup = []
    model = None
    default_this_month = True

    def __init__(self, request, params, model, model_admin):
        if self.model is None:
            raise ImproperlyConfigured(
                "The list filter '%s' does not specify a 'model'."
                % self.__class__.__name__
            )
        super().__init__(request, params, model, model_admin)

    def choices(self, changelist):
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': changelist.get_query_string({self.parameter_name: lookup}),
                'display': title,
            }

    def lookups(self, request, model_admin):
        meses = self.model.objects.dates(self.parameter_name, 'month', order='DESC')
        return [('all', _('Todos'))] + [(date(mes, 'Ym'), date(mes, _('F \d\e Y'))) for mes in meses]

    def value(self):
        value = super().value()
        if value:
            return value
        if self.default_this_month:
            return date(d.today(), 'Ym')
        return 'all'

    def queryset(self, request, queryset):
        if (self.value() == 'all'):
            return queryset
        data = d(int(self.value()[0:4]), int(self.value()[4:6]), 1)
        return queryset.filter(**{
            self.parameter_name + '__month': data.month, self.parameter_name + '__year': data.year,
        })
