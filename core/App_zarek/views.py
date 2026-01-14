from django.shortcuts import render
from .forms import ContactForm
from .models import *
######## mail verzenden #########
from django.core.mail import EmailMessage
from django.views.generic import ListView, DetailView


# ALGEMEEN
def index_view(request):
    return render(request, 'index.html')


### -- PORTFOLIO -- ### 
class OverzichtFoli(ListView):
    model = Portfolio

class DetailFoli(DetailView):
    model = Portfolio
    template_name = 'portfolio_detail.html'

def foli(request):
    folis = Portfolio.objects.all
    return render(request,'portfolio.html', {'folis': folis})
### // PORTFOLIO -- ### 



### CONTACTFORMULIER ###
def contact_view (request):
  print("contactpagina")
  # INFORMATIE # 
  onderwerp = "Email via website Zarekbouw"
  #// INFORMATIE # 
  if request.method == "POST":
      contact_form = ContactForm(request.POST)
      if contact_form.is_valid():
        contact_form.save() # opslaan in admin omgeving
        #EMAIL VERZENDEN#
        email = EmailMessage(
          subject = onderwerp,
          body = contact_form.mail_cf(),
          from_email = 'vikamper@hotmail.com',
          to = ['vikamper@hotmail.com'],
          bcc= ['vikamper@hotmail.com'])
        email.send(fail_silently = False) # op True zetten bij productie 
        print("email verzonden")
        submitted = True
        print('formulier is ingediend > dankbericht verschijnt')
        #//EMAIL VERZENDEN#
  else:
    contact_form = ContactForm()
    pass
  return render(request, 'contact.html', {'contact_form':  contact_form})  
### //CONTACTFORMULIER ###