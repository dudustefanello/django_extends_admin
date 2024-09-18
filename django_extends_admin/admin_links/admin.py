from django_extends_admin.summary_admin.admin import SummaryAdmin


class AdminLinks(SummaryAdmin):
    change_form_template = 'admin_links/change_form_links.html'
    change_list_template = 'admin_links/change_list_links.html'

    def get_change_links(self, request, obj=None):
        """ :rtype: [{'url': str, 'description': str, 'querystring': bool}]
        """
        return None

    def get_list_links(self, request, obj=None):
        """ :rtype: [{'url': str, 'description': str}]
        """
        return None

    def change_view(self, request, object_id, form_url="", extra_context=None):
        view = super().change_view(request, object_id, form_url, extra_context)
        try:
            view.context_data['links'] = self.get_change_links(request, view.context_data['original'])
        except KeyError:
            pass
        except AttributeError:
            pass
        return view

    def changelist_view(self, request, extra_context=None):
        view = super().changelist_view(request, extra_context)
        try:
            view.context_data['links'] = self.get_list_links(request, view.context_data['cl'].queryset)
        except KeyError:
            pass
        except AttributeError:
            pass
        return view
