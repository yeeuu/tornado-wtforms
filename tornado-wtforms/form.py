#!/usr/bin/env python
# coding=utf-8
from __future__ import absolute_import, division, print_function
from weakref import ref

from wtforms import form

from .i18n import TornadoTranslations


class TornadoInputWrapper(object):
    def __init__(self, handler):
        super(TornadoInputWrapper, self).__init__()
        self.handler = ref(handler)

    @property
    def _arguments(self):
        return self.handler().request.arguments

    def __iter__(self):
        return iter(self._arguments)

    def __len__(self):
        return len(self._arguments)

    def __contains__(self, name):
        # We use request.arguments because get_arguments always returns a
        # value regardless of the existence of the key.
        return (name in self._arguments)

    def getlist(self, name, strip=False):
        # get_arguments by default strips whitespace from the input data,
        # so we pass strip=False to stop that in case we need to validate
        # on whitespace.
        return self.handler().get_arguments(name, strip)

    def __getitem__(self, name):
        return self.handler().get_argument(name)


class Form(form.Form):
    """
    A Form derivative which uses the locale module from Tornado.
    """

    def __init__(self, formdata=None, obj=None, prefix='', locale_code='en_US',
                 **kwargs):
        self._locale_code = locale_code
        super(Form, self).__init__(formdata, obj, prefix, **kwargs)

    def process(self, formdata=None, obj=None, **kwargs):
        if formdata is not None:
            formdata = TornadoInputWrapper(formdata)
        super(Form, self).process(formdata, obj, **kwargs)

    def _get_translations(self):
        if not hasattr(self, '_locale_code'):
            self._locale_code = 'en_US'
        return TornadoTranslations(self._locale_code)
