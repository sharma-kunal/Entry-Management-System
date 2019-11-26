from django import forms
import re

PHONE_NUMBER_REGEX = r'^\d{10}$'


class RawForm(forms.Form):
    visitor_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'input',
                                                                                'placeholder': "Visitor's Name"}))
    visitor_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'input',
                                                                   'placeholder': "Visitor's Phone Number"}))
    visitor_email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': "Visitor's Email"}))
    host_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'input',
                                                                             'placeholder': "Host Name"}))
    host_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'input',
                                                                'placeholder': "Host Phone Number"}))
    host_email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': "Host Email"}))

    def clean_host_email(self, *args, **kwargs):
        e1 = self.cleaned_data.get('visitor_email')
        e2 = self.cleaned_data.get('host_email')
        if e1 == e2:
            raise forms.ValidationError("Visitor and Host Email Can't be same")
        return e2

    def clean_host_number(self, *args, **kwargs):
        e1 = self.cleaned_data.get('visitor_number')
        e2 = self.cleaned_data.get('host_number')
        if e1 == e2:
            raise forms.ValidationError("Visitor and Host Phone No. can't be same")
        elif not re.match(PHONE_NUMBER_REGEX, e2):
            raise forms.ValidationError("Please Check the Phone No. you entered")
        return e2

    def clean_visitor_number(self, *args, **kwargs):
        num = self.cleaned_data.get('visitor_number')
        if not re.match(PHONE_NUMBER_REGEX, num):
            raise forms.ValidationError("Please Check the Phone No. you entered")
        return num


class CheckOutForm(forms.Form):
    number = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': "Phone Number"}))

    def clean_number(self):
        num = self.cleaned_data.get('number')
        if not re.match(PHONE_NUMBER_REGEX, num):
            raise forms.ValidationError('Please Check the Phone No. you entered')
        return num
