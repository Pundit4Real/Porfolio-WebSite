from django import forms
from .models.contact import ContactUs
from .models.services import Services

class ContactUsForm(forms.ModelForm):

    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'type':'text',
                'class':'form_group',
                'placeholder':'First name'
            }
        ),
    ) 
    
    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'type':'text',
                'class':'form_group',
                'placeholder':'Last name'
            }
        ),
    ) 
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'type':'email',
                'class':'form_group',
                'placeholder':'Email Address'
            }
        ),
    ) 
    
    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'type':'tel',
                'class':'form_group',
                'placeholder':'Phone'
            }
        ),
    ) 

    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class':'form_group',
                'rows': 4,
                'placeholder':'Enter your message here !'
            }
        ),
    ) 

    service = forms.ModelChoiceField(
        queryset=Services.objects.all(),
        empty_label="Select a service",
        widget=forms.Select(
            attrs={
                'class': 'form_group',
                'placeholder':'Select a service'
            }
        ),
        required=True
    )
    class Meta:
        model = ContactUs
        fields = ['first_name', 'last_name', 'email', 'phone','service','message',]