from django import forms

class ContactMeForm(forms.Form):
    name = forms.CharField(_("Name"), max_length=100, widget=forms.TextInput(
                            attrs={'class':'form-control','placeholder':'Your name....','required':True}))
    email = forms.EmailField(_("Email"), widget=forms.TextInput(
                            attrs={'class':'form-control', 'placeholder':'Your email.....','required':True}))
    subject = forms.CharField(_("Subject"), max_length=70,widget=forms.TextInput(
                                attrs={'class':'form-control','placeholder':'Subject.....','required':True}))
    message = forms.CharField(_("Message"),widget=forms.Textarea(
                            attrs={'class':'form-control','row':5,'placeholder':'Your message......','required':True}))
