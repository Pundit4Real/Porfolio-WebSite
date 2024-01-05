from django import forms

class ContactMeForm(forms.Form):
    name = forms.CharField(_("Name"), max_length=100)
    email = forms.EmailField(_("Email"),)
    subject = forms.CharField(_("Subject"), max_length=70)
    message = forms.CharField(_("Message"),widget=forms.Textarea)
