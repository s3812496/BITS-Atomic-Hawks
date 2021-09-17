from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='E-Mail')
    phone = forms.NumberInput()
    body = forms.CharField(widget=forms.Textarea)