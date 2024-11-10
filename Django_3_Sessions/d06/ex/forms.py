from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Tip, Vote

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.set_password(self.cleaned_data['password1'])
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['reputation']

class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ['content']

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['vote_type']
