from django import forms

class inputForm(forms.Form):
    text = forms.CharField(max_length=10000,widget=forms.Textarea,required=False)
    file = forms.FileField(required=False) 