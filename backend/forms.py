from django import forms
from .models.contact import ContactUs
from .models.services import Services

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['first_name', 'last_name', 'email', 'phone', 'message', 'service']
        
        widgets = {
            'service': forms.Select(
                attrs={
                    'class': 'form-control'
                    }
               ),
            }

    def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        self.fields['service'].queryset = Services.objects.all()
