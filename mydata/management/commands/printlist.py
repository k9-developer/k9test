from django.core.management.base import NoArgsCommand
from django.contrib.contenttypes.models import ContentType

class Command(NoArgsCommand):
    help = "Can be run directly"

    def handle_noargs(self, **options):
        for obj in ContentType.objects.all():
            print "Model: %s , count - %s." % \
                (obj.model_class(), obj.model_class().objects.count())