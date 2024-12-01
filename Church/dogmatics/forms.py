from mdeditor.fields import MDTextFormField
from django import forms 

class PreprintForm(forms.Form):
    title = forms.CharField(max_length=128,empty_value=False)
    abstract = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}), max_length=512, empty_value=False)
    content = MDTextFormField() #バリデーションどうする？

