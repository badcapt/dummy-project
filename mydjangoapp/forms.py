from django import forms
from django.forms.widgets import Widget
from mydjangoapp.models import Accesspage,Topic,Webpage


class forname(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

class newForm(forms.ModelForm):
    class Meta:
        model = Webpage
        fields = "__all__"  

