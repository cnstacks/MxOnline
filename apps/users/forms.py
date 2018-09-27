#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: MxOnline 
# Software: PyCharm
# Time    : 2018-09-26 22:45
# File    : forms.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from django import forms


class LoginForm():
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
