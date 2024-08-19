from django import forms
from .models import People

class SearchForm(forms.Form):
    min_release_date = forms.DateField(label='Movies minimum release date', widget=forms.SelectDateWidget(years=range(1900, 2101)))
    max_release_date = forms.DateField(label='Movies maximum release date', widget=forms.SelectDateWidget(years=range(1900, 2101)))
    min_planet_diameter = forms.IntegerField(label='Planet diameter greater than')
    character_gender = forms.ChoiceField(label='Character gender', choices=[], required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genders = list(People.objects.values_list('gender', flat=True).distinct())
        
        print(f"Genders found in DB: {genders}")

        if not genders:
            self.fields['character_gender'].choices = [('default', 'No Gender Available')]
            self.initial['character_gender'] = 'default'
        else:
            self.fields['character_gender'].choices = [(gender, gender) for gender in genders]
            self.initial['character_gender'] = genders[0]  # Set the first gender as default
