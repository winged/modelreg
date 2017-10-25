#!/usr/bin/env python3

"""Documentation about the module... may be multi-line"""

from django.utils.translation import ugettext_lazy as _
from random import SystemRandom
import string
import json
import base64
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user  = models.OneToOneField(User, related_name='profile')

    address = models.TextField()
    phone   = models.CharField(max_length=50)


def make_identifier(length=15):
    letters = string.ascii_letters + string.digits + string.ascii_lowercase
    return ''.join(SystemRandom().choice(letters) for _ in range(length))


class PublicProfile(models.Model):

    user        = models.OneToOneField(User, related_name='public_profile')
    public_info = models.TextField()
    identifier  = models.CharField(max_length=15, default=make_identifier, blank=True)
    auth        = models.CharField(max_length=15, default=make_identifier, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['identifier', 'auth']),
        ]


class Case(models.Model):

    TYPE_CHOICES = (
        ('no_damage', _('No Damage')),
        ('property_damage', _('Property Damage')),
        ('injury', _('Injury')),
    )

    damage_type  = models.CharField(max_length=20, choices=TYPE_CHOICES, default='no_damage')

    model_owner    = models.ForeignKey(User, related_name='cases')
    identifier     = models.CharField(max_length=15, default=make_identifier, blank=True)
    timestamp      = models.DateTimeField(auto_now_add=True)

    owner_resolved  = models.BooleanField(default=False)
    finder_resolved = models.BooleanField(default=False)
    admin_informed  = models.BooleanField(default=False)

    reporter_email = models.EmailField()

    class Meta:
        indexes = [
            models.Index(fields=['identifier']),
        ]


class CaseMessage(models.Model):

    SENDER_CHOICES=(
        ('admin', _('Administrator')),
        ('finder', _('Finder')),
        ('owner', _('Owner')),
    )

    case       = models.ForeignKey(Case, related_name = 'messages')
    timestamp  = models.DateTimeField(auto_now_add=True)
    for_admin  = models.BooleanField(default=False)
    message    = models.TextField()

    sender = models.CharField(max_length=10, choices=SENDER_CHOICES)

    @property
    def from_owner(self):
        return self.sender == 'owner'


    class Meta:
        indexes = [
            models.Index(fields=['timestamp']),
        ]

