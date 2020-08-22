from django import forms

# from .models import

class UserInputForm(forms.Form):
    currency1= forms.CharField(max_length= 250,label="From")
    currency2 = forms.CharField(max_length=250, label="To")
    value= forms.FloatField( label="Enter the Value")
