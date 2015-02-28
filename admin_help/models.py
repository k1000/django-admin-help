from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.core import urlresolvers


class Page(models.Model):
    content_type = models.ForeignKey(ContentType, unique=True)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField()

    def get_admin_add(self):
        return urlresolvers.reverse(
            "admin:%s_%s_add" % (self.content_type.app_label, self.content_type.model))

    def __unicode__(self):
        return str(self.content_type)


POSITIONS = ("bottom", "top", "left", "right")


class Step(models.Model):
    page = models.ForeignKey(Page)
    order = models.PositiveSmallIntegerField()
    element = models.CharField(
        max_length=150,
        blank=True, null=True)
    position = models.CharField(
        choices=zip(POSITIONS, POSITIONS), max_length=25)
    intro = models.TextField()

    class Meta:
        ordering = ('order', )
