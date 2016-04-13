<<<<<<< HEAD
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class School(models.Model):
    name = models.CharField(max_length=100)


class Parent(models.Model):
    name = models.CharField(max_length=100)


class Child(models.Model):
    mother = models.ForeignKey(Parent, models.CASCADE, related_name='mothers_children')
    father = models.ForeignKey(Parent, models.CASCADE, related_name='fathers_children')
    school = models.ForeignKey(School, models.CASCADE)
    name = models.CharField(max_length=100)


@python_2_unicode_compatible
class Poet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Poem(models.Model):
    poet = models.ForeignKey(Poet, models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
=======
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class School(models.Model):
    name = models.CharField(max_length=100)


class Parent(models.Model):
    name = models.CharField(max_length=100)


class Child(models.Model):
    mother = models.ForeignKey(Parent, models.CASCADE, related_name='mothers_children')
    father = models.ForeignKey(Parent, models.CASCADE, related_name='fathers_children')
    school = models.ForeignKey(School, models.CASCADE)
    name = models.CharField(max_length=100)


@python_2_unicode_compatible
class Poet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Poem(models.Model):
    poet = models.ForeignKey(Poet, models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('poet', 'name')

    def __str__(self):
        return self.name
>>>>>>> 6448873197fa4e3df3f5f03201538dc57d7643d6
