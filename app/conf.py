#! /usr/bin/python
# -*- coding: UTF-8 -*-
"""
Global variables for base module
"""
from django.conf import LazySettings
from django.utils.translation import ugettext_lazy as _

settings = LazySettings()


def get_from_settings_or_default(var_name, default):
    try:
        return settings.__getattr__(var_name)
    except AttributeError:
        return default


# Items by page on paginator views
ITEMS_BY_PAGE = 10

CREATE_SUFFIX = "_create"
LIST_SUFFIX = "_list"
DETAIL_SUFFIX = "_detail"
UPDATE_SUFFIX = "_update"
DELETE_SUFFIX = "_delete"

API_SUFFIX = "_api"
style = "base_django/flexbox"

# Messages
OBJECT_CREATED_SUCCESSFULLY = _("Object created successfully")
OBJECT_UPDATED_SUCCESSFULLY = _("Object updated successfully")
OBJECT_DELETED_SUCCESSFULLY = _("Object deleted successfully")

BASE_MODELS_TRANSLATION_NAME = _("Name")
BASE_MODELS_TRANSLATION_DESCRIPTION = _("Description")
BASE_MODELS_TRANSLATION_SLUG = _("Slug")
BASE_MODELS_TRANSLATION_CREATED = _("Created")
BASE_MODELS_TRANSLATION_MODIFIED = _("Modified")
BASE_MODELS_TRANSLATION_ACTIVE = _("Active")

CONFIGURING_APPLICATION = _("Configuring application {}")
CREATING_PERMISSION_WITH_NAME = _("Creating Permission with name {}")
CREATING_GROUP_WITH_NAME = _("Creating Group with name {}")

TASK_PREFIX = "TASK"

TASK_VERBOSE_NAME = _("Task")
TASK_VERBOSE_NAME_PLURAL = _("Task")

TASK_LIST_URL_NAME = TASK_PREFIX + LIST_SUFFIX
TASK_CREATE_URL_NAME = TASK_PREFIX + CREATE_SUFFIX
TASK_DETAIL_URL_NAME = TASK_PREFIX + DETAIL_SUFFIX
TASK_UPDATE_URL_NAME = TASK_PREFIX + UPDATE_SUFFIX
TASK_DELETE_URL_NAME = TASK_PREFIX + DELETE_SUFFIX
TASK_LIST_JSON_URL_NAME = TASK_PREFIX + '_list_json'
