from django import template

register = template.Library()

@register.simple_tag
def get_edit_url(object):
    return "/admin/" + object._meta.app_label + "/" + object._meta.module_name + "/" + str(object.id) + "/" 

