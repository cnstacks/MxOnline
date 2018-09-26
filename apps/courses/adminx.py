#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: MxOnline 
# Software: PyCharm
# Time    : 2018-09-26 11:53
# File    : adminx.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
import xadmin
from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    search_fileds = ['name', 'desc', 'detail', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']


class LessonAdmin(object):
    list_display = ['course', 'name', 'learn_times', 'add_time']
    search_fileds = ['course', 'name', 'learn_times']
    list_filter = ['course__name', 'name', 'learn_times', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'learn_times', 'url', 'add_time']
    search_fileds = ['lesson', 'name', 'learn_times', 'url']
    list_filter = ['lesson', 'name', 'learn_times', 'url', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fileds = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
