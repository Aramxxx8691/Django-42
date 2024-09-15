from django import forms
from .models import Tip

class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Enter your tip here...',
                'rows': 3,
                'class': 'form-control'
            })
        }
