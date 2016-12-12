from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    secret_key = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return self.name


class Match(models.Model):
    gifter = models.ForeignKey(Person, db_column='gifter_id', related_name='+')
    giftee = models.ForeignKey(Person, db_column='giftee_id', related_name='+')

    def __str__(self):
        return self.gifter.name + " :: " + self.giftee.name
