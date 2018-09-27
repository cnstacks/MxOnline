#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: MxOnline 
# Software: PyCharm
# Time    : 2018-09-26 22:45
# File    : forms.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField()
