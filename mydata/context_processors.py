
def settings_add(request):
    from django.conf import settings
    return {'settings': settings}
