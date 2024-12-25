from django import forms

class DonationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    message = forms.CharField(widget=forms.Textarea, required=False)
