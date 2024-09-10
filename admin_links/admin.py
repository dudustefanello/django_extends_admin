from django.contrib import admin


class AdminLinks(admin.ModelAdmin):
    change_form_template = 'admin_links/change_form.html'

    def get_links(self, request, obj=None):
        """ :rtype: [{'url': str, 'description': str}]
        """
        return None

    def change_view(self, request, object_id, form_url="", extra_context=None):
        view = super().change_view(request, object_id, form_url, extra_context)
        try:
            view.context_data['links'] = self.get_links(request, view.context_data['original'])
        except KeyError or AttributeError:
            pass
        return view