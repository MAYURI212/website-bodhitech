from django import forms

class ContactForm(forms.Form):
    f_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'f_name'}),label='Your First Name',max_length=50,min_length=4,required=True) 
    l_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'l_name'}),label='Your last name',max_length=50,min_length=4,required=True)
    mobile_no=forms.CharField(widget=forms.NumberInput(attrs={'placeholder':'mobile_no'}),label='Your mobile_no',max_length=10,min_length=10,required=True)
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}),label='Your Email',max_length=50,min_length=8,required=True)
    address=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'email'}),label='Your adress',max_length=100,min_length=50,required=True)
    subject=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject'}),label='Subject',max_length=50,min_length=8,required=True)