from django import forms
from api.models import Ad_type
from api.models import Ads, UserDetail


class AdsValidation(forms.ModelForm):
    class Meta:
        model = Ads
        fields = ['ad_type']

    def __init__(self, *args, **kwargs):
        ad_id = kwargs.pop('ad_type')
        print(ad_id)
        super(AdsValidation, self).__init__(*args, **kwargs)
        self.fields['ad_type'].queryset = Ad_type.objects.all()
        #self.fields['author']=forms.ModelChoiceField(queryset=UserDetail.objects.filter(token=token))
