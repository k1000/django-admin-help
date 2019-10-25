from django.db import models
from django.contrib.contenttypes.models import ContentType
#from django.core import urlresolvers


class Page(models.Model):
    path = models.CharField(
        max_length= 255,
        help_text="full path ex '/admin/admin_help/page/add/'")
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField()

    def __unicode__(self):
        return str(self.path)


POSITIONS = ("bottom", "top", "left", "right")


class Step(models.Model):
    page = models.ForeignKey(Page)
    order = models.PositiveSmallIntegerField()
    element = models.CharField(
        max_length=150,
        blank=True, null=True)
    position = models.CharField(
        default="bottom",
        choices=zip(POSITIONS, POSITIONS), max_length=25)
    desc = models.TextField("description")

    class Meta:
        ordering = ('order', )
