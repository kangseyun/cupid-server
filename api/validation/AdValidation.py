from django import forms

class AdsValidation(forms.Form):
    ad_type = forms.IntegerField()
    title = forms.CharField()
    budget = forms.IntegerField()
    limit = forms.IntegerField()