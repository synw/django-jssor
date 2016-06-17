# -*- coding: utf-8 -*-

from django import forms
from codemirror2.widgets import CodeMirrorEditor
from jssor.models import Slide


class JssorAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JssorAdminForm, self).__init__(*args, **kwargs)
    
    html = forms.CharField(
                              widget=CodeMirrorEditor(options={
                                                         'mode':'htmlmixed',
                                                         'width':'1170px',
                                                         'indentWithTabs':'true', 
                                                         #'indentUnit' : '4',
                                                         'lineNumbers':'true',
                                                         'autofocus':'true',
                                                         #'highlightSelectionMatches': '{showToken: /\w/, annotateScrollbar: true}',
                                                         'styleActiveLine': 'true',
                                                         'autoCloseTags': 'true',
                                                         #'keyMap': CODEMIRROR_KEYMAP,
                                                         'theme':'blackboard',
                                                         }, 
                                                         modes=['css', 'xml', 'javascript', 'htmlmixed'],
                                                         )
                              
                              )
    
    class Meta:
        model = Slide
        exclude = ('created','edited')
