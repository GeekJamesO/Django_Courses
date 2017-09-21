from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import *
from django.contrib import messages

def index(request):
    context = { 'courses' : Course.objects.all() }
    return render(request, "DojoCourses_app/index.html", context)

def destroy(request, courseId):
    thisCourse = None
    try:
        thisCourse = Course.objects.get(id=courseId)
    except Exception as e:
        pass
    print "Course = ",  thisCourse
    if None == thisCourse:
        messages.error(request, "No Course with number {} Exists.. error.".format(courseId))
    else:
        thisCourse.delete()
        thisCourse = None
        messages.info(request, "Course '{}' deleted.".format(courseId))
    context = { }
    return render(request, "DojoCourses_app/destroy.html", context)

def yesDestroy(request, courseId):
    thisCourse = None
    try:
        thisCourse = Course.objects.get(id=courseId)
    except Exception as e:
        pass
    print "Course = ",  thisCourse
    if None == thisCourse:
        messages.error(request, "No Course with number {} Exists.. error.".format(courseId))
    else:
        thisCourse.delete()
        thisCourse = None
        messages.info(request, "Course '{}' deleted.".format(courseId))
    context = { }
    return redirect('/')

def addcourse(request):
    name = request.POST['name']
    description = request.POST['description']
    results = Course.objects.Creator(name, description)
    if len(results['errors']) > 0:
        for aStr in results['errors']:
            messages.error(request, aStr)
    if None == results['CourseObj']:
        messages.error(request, "No Course object created.")
    else:
        messages.info(request, str(results['CourseObj']))
    return redirect('/')
