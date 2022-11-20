from django import forms
from .import models

class MyFileForm(forms.Form):
    name=forms.CharField(max_length=50)
    file=forms.FileField()

    class Meta:
        model = models.MyFileUpload
        fields = ['name', 'file']