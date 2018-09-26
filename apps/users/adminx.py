#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: MxOnline 
# Software: PyCharm
# Time    : 2018-09-26 11:18
# File    : adminx.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
import xadmin
from .models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    pass


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
