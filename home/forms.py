from django import forms

class FormQuery(forms.Form):
    query=forms.CharField()