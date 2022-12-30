#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.apps import apps
from django.contrib import admin

# Register your models here.

from app.models import *


class TaskAdmin(admin.ModelAdmin):
    list_filter = []
    search_fields = (
        'id',
    )
    inlines = []
    list_display = ("id", "title", "category", "completed", "date")


admin.site.register(Task, TaskAdmin)
