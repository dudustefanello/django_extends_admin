from django.contrib import admin


class SummaryAdmin(admin.ModelAdmin):
    change_list_template = 'summary_admin/summary_change_list.html'

    def get_summary(self, request, queryset=None):
        """ :rtype: {'field_name': Decimal}
        """
        return None

    def changelist_view(self, request, extra_context=None):
        view = super().changelist_view(request, extra_context)
        try:
            view.context_data['summary'] = self.get_summary(request, view.context_data['cl'].queryset)
        except KeyError:
            pass
        except AttributeError:
            pass
        return view
