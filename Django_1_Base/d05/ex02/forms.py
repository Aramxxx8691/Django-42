from django import forms

class History(forms.Form):
    history = forms.CharField(label='text', max_length=100)
