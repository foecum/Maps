from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from .utils import code_generator, create_shortcode

SHORT_CODE_MAX = getattr(settings, 'SHORTCODE_MAX', 15)

class GittaURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(GittaURLManager, self).all(*args, **kwargs)
        qs = qs.filter(active=True)
        return qs

    def refresh_shortcodes(self):
        qs = GittaURL.objects.filter(pk__gte=1)
        new_code = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            new_code += 1
        return 'New codes made: {i}'.format(i=new_code)

class GittaURL(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=20,unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = GittaURLManager()

    def save(self, *args, **kwargs):
        print self.shortcode
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(GittaURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
