from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class searchForm(forms.Form):
    General_Search = forms.CharField(
        required=False, max_length=400)
    Title = forms.CharField(required=False, max_length=400)
    NASA_ID = forms.CharField(required=False, max_length=400)
    Key_Words = forms.CharField(required=False, max_length=400)
    Lower_Year_Bound = forms.IntegerField(required=False, help_text='(YYYY)')
    Upper_Year_Bound = forms.IntegerField(required=False, help_text='(YYYY)')
