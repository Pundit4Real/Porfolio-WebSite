from django import forms

class ContactMeForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your name...',
                'required': True,
                'id': 'name' 
            }
        )
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your email...',
                'required': True,
                'id': 'email' 
            }
        )
    )
    
    subject = forms.CharField(
        max_length=70,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Subject...',
                'required': True,
                'id': 'subject' 
            }
        )
    )
    
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 6,  
                'placeholder': 'Your message...',
                'id': 'message'  
            }
        )
    )
