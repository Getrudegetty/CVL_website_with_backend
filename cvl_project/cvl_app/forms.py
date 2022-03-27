from email import message
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    firstname = forms.CharField(max_length=100, required=True, 
            widget=forms.TextInput(attrs={
                'placeholder': '*First Name..',
                'class': 'form-control'
            }))
    lastname = forms.CharField(max_length=100, required=True, 
            widget=forms.TextInput(attrs={
                'placeholder': '*Last Name..',
                'class': 'form-control'
            }))
    email = forms.EmailField(max_length=254, required=True, 
            widget=forms.TextInput(attrs={
                'placeholder': '*Email..',
                'class': 'form-control'
            }))
    phone = forms.IntegerField(required=True, 
            widget=forms.NumberInput(attrs={
                'placeholder': '*Phone Number..',
                'class': 'form-control'
            }))
    message = forms.CharField(max_length=1000, required=True, 
            widget=forms.Textarea(attrs={
                'placeholder': '*Your Message..',
                'rows': 8,
                'class': 'form-control'
            }))
           
    class Meta:
        model = Contact
        fields = ('firstname', 'lastname', 'email', 'phone', 'message',)