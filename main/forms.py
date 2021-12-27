from django import forms

class CreateNewPassword(forms.Form):
    digits = forms.IntegerField(label="Number of digits in the password", max_value=100)
    digits.widget = forms.NumberInput(attrs={'id': 'number_field', 'style': 'width:10ch'})

    check = forms.BooleanField(label="Lower case", required=False, initial=False)
    check.widget = forms.CheckboxInput(attrs={'class': 'custom-group'})

    check1 = forms.BooleanField(label="Upper case", required=False, initial=False)
    check1.widget = forms.CheckboxInput(attrs={'class': 'form-group'})

    check2 = forms.BooleanField(label="Numbers", required=False, initial=False)
    check2.widget = forms.CheckboxInput(attrs={'class': 'form-group'})

    check3 = forms.BooleanField(label="Special Characters", required=False, initial=False)
    check3.widget = forms.CheckboxInput(attrs={'class': 'form-group'})

