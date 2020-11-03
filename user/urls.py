#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from django.conf.urls import url

from user.views import reg

urlpatterns = [
    url(r'reg$', reg)
]
