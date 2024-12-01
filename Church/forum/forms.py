from django import forms 

class DiscussionForm(forms.Form):
    
    text = forms.CharField(label="Content", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}), max_length=1024, empty_value=False)

class DiscussionForm_guest(forms.Form):
    guest_name = forms.CharField(label="Guest name",widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}),max_length=32, empty_value=False)
    text = forms.CharField(label="Content", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}), max_length=1024, empty_value=False)


class PageForm(forms.Form):
    page_number = forms.IntegerField(label="Enter Chapter Number",required=True)


