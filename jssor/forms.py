# -*- coding: utf-8 -*-

from django import forms
#from codemirror2.widgets import CodeMirrorEditor
from jssor.models import Slide


class JssorAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JssorAdminForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Slide
        exclude = ('created','edited')
