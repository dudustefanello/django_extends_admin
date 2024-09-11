from django.contrib import admin
from django.db.models import Sum

from admin_links.admin import AdminLinks
from just_test.models import NumericModel


@admin.register(NumericModel)
class NumericModelAdmin(AdminLinks):
    list_display = ['id', 'descricao', 'valor']

    def get_summary(self, request, queryset=None):
        return {
            'valor': queryset.all().aggregate(valor=Sum('valor'))['valor'],
        }

    def get_change_links(self, request, obj=None):
        return [{
            'url': 'https://google.com/', 'description': 'Google',
        }]

    def get_list_links(self, request, obj=None):
        """ :rtype: [{'url': str, 'description': str}]
        """
        return self.get_change_links(request, obj)
