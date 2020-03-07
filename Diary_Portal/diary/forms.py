from django import forms

class save_changes(forms.Form):
    POC = forms.CharField(max_length=100)
    CPOC = forms.CharField(max_length=100)
    Remark = forms.CharField(widget=forms.Textarea)

class add_company(forms.Form):
    CompanyName = forms.CharField(max_length=100)
    POC = forms.CharField(max_length=100)
    CPOC = forms.CharField(max_length=100)
    Remark = forms.CharField(widget=forms.Textarea)

class authentication(forms.Form):
    Username = forms.CharField(max_length=100)
    Password = forms.CharField(max_length=100)
