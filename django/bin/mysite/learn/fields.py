# -*- coding: utf-8 -*-
# @Date    : 2015-06-09 13:02:04
# @Author  : Weizhong Tu (mail@tuweizhong.com)
# @Link    : http://www.tuweizhong.com

from django.db import models
import ast


class CompressedTextField(models.TextField):
    """    model Fields for storing text in a compressed format (bz2 by default)    """
    __metaclass__ = models.SubfieldBase
 
    def to_python(self, value):
        if not value:
            return value
 
        try:
            return value.decode('base64').decode('bz2').decode('utf-8')
        except Exception:
            return value
 
    def get_prep_value(self, value):
        if not value:
            return value
 
        try:
            value.decode('base64')
            return value
        except Exception:
            try:
                tmp = value.encode('utf-8').encode('bz2').encode('base64')
            except Exception:
                return value
            else:
                if len(tmp) > len(value):
                    return value
                return tmp


class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"
 
    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)
 
    def to_python(self, value):
        if not value:
            value = []
 
        if isinstance(value, list):
            return value
 
        return ast.literal_eval(value)
 
    def get_prep_value(self, value):
        if value is None:
            return value
 
        return unicode(value)
 
    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)
