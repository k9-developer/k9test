# coding: utf-8
from django.db import models
from datetime import datetime
from django.db.models import signals


PRIORITY_CHOICES =(
    ('0', '0'),
    ('1', '1'),
)


class MyData(models.Model):
    name = models.CharField('Name', max_length=20,)
    last_name = models.CharField('Last Name', max_length=20,)
    birthday = models.DateField()
    bio = models.TextField('Bio',)
    email = models.EmailField()


class HttpReq(models.Model):
    path = models.CharField('Path', max_length=200,)
    time = models.DateTimeField('Time', default=datetime.now(),)
    priority = models.CharField('Priority', max_length=1, blank=True,
            default='', choices=PRIORITY_CHOICES,)

    def __unicode__(self):
        return u"(%s) %s %s [%s]" %\
            (self.id, self.time, self.path, self.priority)


class Logging(models.Model):
    action_time = models.DateTimeField('action time',
            auto_now_add=True, default=datetime.now,)
    action = models.CharField('action',
            max_length=200, blank=True, null=True,)
    object_id = models.CharField('object id',
            max_length=200, blank=True, null=True,)
    object_repr = models.CharField('object repr',
            max_length=200, blank=True, null=True,)

    class Meta:
        ordering = ('-action_time',)

    def __unicode__(self):
        return u"(%s) %s %s, %s id: %s" %\
            (self.id, self.action, self.action_time, self.object_repr, self.object_id)


def my_post_save(sender, instance, created, **kwargs):
    log = Logging()
    log.object_id = instance.id
    log.object_repr = instance._meta.module_name
    if created:
        log.action = "created"
    else:
        log.action = "edited"
    log.save()

def my_post_delete(sender, instance, **kwargs):
    log = Logging()
    log.object_id = instance.id
    log.object_repr = instance._meta.module_name
    log.action = 'deleted'
    log.save()

signals.post_save.connect(my_post_save, sender=MyData)
signals.post_delete.connect(my_post_delete, sender=MyData)

signals.post_save.connect(my_post_save, sender=HttpReq)
signals.post_delete.connect(my_post_delete, sender=HttpReq)