# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from app.utils import answer_filter


class Event(models.Model):
    name = models.CharField(max_length=32)
    key = models.CharField(max_length=32, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    starttime = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.key = self.key.upper()
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return "{0.name} ({0.key})".format(self)


class Question(models.Model):
    image = models.ImageField()
    answer = models.CharField(max_length=32)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True)

    def save(self, *args, **kwargs):
        self.answer = answer_filter(self.answer)
        super(Question, self).save(*args, **kwargs)


class Player(models.Model):
    username = models.CharField(max_length=30, unique=True)
    score = models.FloatField(default=0)

    def __str__(self):
        return ' {"%s" : "%s"}' % (self.username, self.score)


class Input(models.Model):
    user = models.ForeignKey(Player, on_delete=models.CASCADE)
    word = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return '{"%s" : "%s"}' % (self.user.username, self.word)

    def save(self, *args, **kwargs):
        self.word = answer_filter(self.answer)
        super(Input, self).save(*args, **kwargs)





