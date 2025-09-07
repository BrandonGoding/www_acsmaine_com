from django import forms


class ServiceRequestForm(forms.Form):
    name = forms.CharField(max_length=100)
    service_address = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=50)
    email = forms.EmailField()
    work_desired = forms.CharField(widget=forms.Textarea)
