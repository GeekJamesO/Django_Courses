# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# shell  from apps.DojoCourses_app.models import *
#        p1 = Course.objects.Creator("Python 123","This description should be long enough")
class CourseDescriptionManager(models.Manager):
    def Creator(self, desc):
        newDescription = None
        errors = self.validate(desc)
        if len(errors) == 0:
            newDescription = CourseDescription.objects.create()
            newDescription.description = desc
            # NO SAVE here on purpose..
        return { 'DescObj' : newDescription, 'errors' : errors }

    # Validate returns errors as string array, empty list when valid.
    def validate(self, desc):
        MinLen = 16
        MaxLen = 400
        errorlist = []
        if len(desc) < MinLen:
            errorlist += [ "Decription is too short, must be atleast {} characters".format(MinLen) ]
        if len(desc) > MaxLen:
            errorlist += [ "Decription is too long, must be no more than {} characters".format(MaxLen) ]
        return errorlist
class CourseDescription(models.Model):
    description = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseDescriptionManager()
    def __str__(self):
        return "desc = '{}' ".format(self.description)

class CourseManager(models.Manager):
    def Creator(self, name, desc):
        errors = self.validate(name, desc)
        newCourse = None
        if len(errors) == 0:
            result = CourseDescription.objects.Creator(desc)
            newDescription = result['DescObj']
            errors += result['errors']
            newCourse = Course.objects.create()
            newCourse.name = name
            # setup both 1 way foreign keys.
            # newDescription.courseObj = newCourse
            newCourse.DescObj = newDescription
            newDescription.save()
            newCourse.save()
        return { 'CourseObj' : newCourse, 'errors' : errors }
    # Validate returns errors as string array, empty list when valid.
    def validate(self, name, desc):
        MinLen = 5
        MaxLen = 55
        errorlist = []
        if len(name) < MinLen:
            errorlist += [ "Name is too short, must be atleast {} characters".format(MinLen) ]
        if len(name) > MaxLen:
            errorlist += [ "Name is too long, must be no more than {} characters".format(MaxLen) ]
        errorlist += CourseDescription.objects.validate(desc)
        return errorlist
    def getById(self, courseId):
        return Course.objects.get(id = courseId)

class Course(models.Model):
    name = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()
    DescObj = models.OneToOneField(
        CourseDescription,
        on_delete=models.CASCADE,
        null=True,
        related_name="courseObj",
    )
    def __str__(self):
        descString = "--empty--"
        if None != self.DescObj:
            descString = self.DescObj
        return "name:'{}' {} > ".format(self.name, descString)
