from django import forms
from .models import *


#### CONTACTFORMULIER###
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        labels = {
            'naam':'Naam',
            'email':'Email',
            'bericht': 'Bericht',}
        widgets = {
            'naam':forms.TextInput(attrs={'class':'form_eigenA1', 'placeholder':'Naam', 'id': '',}),
            'email':forms.TextInput(attrs={'class':'form_eigenA2', 'placeholder':'Email', 'id': '',}),
            'bericht':forms.TextInput(attrs={'class':'form_eigenB', 'placeholder':'Stel hier uw vraag of opmerking.', 'id': '',}),}


    def mail_cf(self):
            print('invulling van email is gereed')
            #invulling van email - verzonden via views.py
            naam = self.cleaned_data.get('naam','leeg' )
            email = self.cleaned_data.get('email','leeg' )
            bericht = self.cleaned_data.get('bericht', 'leeg')
         
            return (
                f"Afz: {naam} \n"
                f"Beste ZarekBouw,\n"
                f"Via het formulier op de website benader ik u.\n"
                f"Mijn vraag is als volgt: {bericht}. \n"
                f"Dit zijn mijn gegevens:\n\n"
                f"Naam: {naam}\n"
                f"Emailgegevens: {email}\n"
                f"Telefoonnr: {email}\n")
                
#### CONTACTFORMULIER###