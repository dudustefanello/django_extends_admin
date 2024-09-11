from django.contrib import admin


class SummaryAdmin(admin.ModelAdmin):
    change_list_template = 'summary_admin/summary_change_list.html'

    def get_summary(self, request, queryset=None):
        """ :rtype: {'header_text': Decimal}
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


class SummaryTabularInline(admin.TabularInline):
    template = 'summary_admin/summary_tabular.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = None

    def get_queryset(self, request):
        if self.queryset:
            return self.queryset
        return super().get_queryset(request)

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        self.queryset = self.get_queryset(request)
        if self.queryset:
            setattr(formset, 'summary', self.get_summary(request, self.queryset.filter(**{formset.fk.name: obj})))
        return formset

    def get_summary(self, request, queryset=None):
        """ :rtype: {'field_name': Decimal}
        """
        return None
