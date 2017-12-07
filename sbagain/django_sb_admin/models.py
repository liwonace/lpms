from __future__ import unicode_literals
from django.db import models
# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Childgroups(models.Model):
    child = models.ForeignKey('Group', models.DO_NOTHING,
related_name='child_childgroups_set')
    parent = models.ForeignKey('Group', models.DO_NOTHING,
related_name='parent_childgroups_set')

    class Meta:
        managed = False
        db_table = 'childgroups'
        unique_together = (('child', 'parent'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Group(models.Model):
    name = models.CharField(unique=True, max_length=255)
    variables = models.TextField(blank=True, null=True)
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'group'


class Host(models.Model):
    host = models.CharField(unique=True, max_length=255)
    hostname = models.CharField(unique=True, max_length=255)
    variables = models.TextField(blank=True, null=True)
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'host'


class Hostgroups(models.Model):
    host = models.ForeignKey(Host, models.DO_NOTHING)
    group = models.ForeignKey(Group, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hostgroups'
        unique_together = (('host', 'group'),)

		
class Hostinfo(models.Model):
    host = models.CharField(unique=True, max_length=255)
    distribution = models.CharField(max_length=255)
    success_count= models.IntegerField()
    fail_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hostinfo'

		
class Inventory(models.Model):
    group = models.CharField(unique=True, max_length=255)
    host = models.CharField(max_length=255)
    hostname = models.CharField(max_length=255)
    host_vars = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory'
