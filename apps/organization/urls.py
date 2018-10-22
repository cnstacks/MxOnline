#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: MxOnline 
# Software: PyCharm
# DateTime: 2018-10-22 22:03
# File: urls.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org

from django.conf.urls import url, include
from .views import OrgView

urlpatterns = [

    # 课程机构首页;
    url(r'^org_list/$', OrgView.as_view(), name="org_list"),

]
