# -*- coding: utf-8 -*-
from django import forms
from .models import Form

class HelloForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['name','mail','gender','age','birthday','egg','shrimp','clab','milk','wheat','soba','peanuts']
    