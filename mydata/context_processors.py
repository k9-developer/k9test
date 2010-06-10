from django.conf import settings

def settings_add(request):
    return {'settings': settings}
