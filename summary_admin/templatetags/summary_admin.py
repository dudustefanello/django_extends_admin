from django.template.defaulttags import register as register_tag
from django.utils.formats import number_format
from django.contrib.admin.templatetags.admin_list import result_list
from django.contrib.admin.templatetags.base import InclusionAdminNode
from django.template import Library

register = Library()


@register_tag.filter
def decimal_format(decimal, places):
    return number_format(round(decimal, places), decimal_pos=places, force_grouping=True)


@register_tag.filter
def get_dict_item_column(dictionary, key):
    return dictionary.get(key)


def summary_result_list(context, cl):
    result = result_list(cl)
    result.update({'context': context})
    return result


@register.tag(name='summary_result_list')
def summary_result_list_tag(parser, token):
    return InclusionAdminNode(
        parser, token,
        func=summary_result_list,
        template_name='../summary_admin/summary_change_list_results.html',
        takes_context=True,
    )
