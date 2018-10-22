#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: MxOnline 
# Software: PyCharm
# DateTime: 2018-10-22 21:57
# File: forms.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org

from django import forms
from operation.models import UserAsk


class AnotherUserForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ["name", "mobile", "course_name"]
