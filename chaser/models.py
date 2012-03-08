from django.db import models
from django.contrib.auth.models import User

class Chaser(models.Model):
    name = models.CharField(max_length=255)
    year_in_school = models.CharField(max_length=50, blank=True, null=True)
    narrative = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to="photos/", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.name

class Report(models.Model):
    chaser = models.ForeignKey(Chaser)
    user = models.ForeignKey(User)
    report = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return "report on %s from %s" % (self.chaser.name, self.user.username)
