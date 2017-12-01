# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import mongoengine
# Create your models here.
class Places(mongoengine.Document):
    address = mongoengine.StringField(required=True)
    createdAt = mongoengine.DateTimeField()
    id = mongoengine.StringField()
    location = mongoengine.DictField()
