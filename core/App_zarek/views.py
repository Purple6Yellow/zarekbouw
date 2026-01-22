from django.shortcuts import render
from .forms import ContactForm
from .models import *
######## mail verzenden #########
from django.core.mail import EmailMessage
from django.views.generic import ListView, DetailView
from django.shortcuts import render ### slideshow portfolio_detail
from django.db.models.fields.files import ImageField

# ALGEMEEN
def index_view(request):
    return render(request, 'index.html')


### -- PORTFOLIO -- ### 
class OverzichtFoli(ListView):
    model = Portfolio

    template_name = "portfolio.html"
    context_object_name = "folis"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        qs = context ["object_list"]
        context["image_urls"] = list(qs.values_list("afbeeld1", flat = True))

        return context

class DetailFoli(DetailView):
    model = Portfolio
    context_object_name = "foli_detail"
    template_name = "portfolio_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        foli_detail = self.object

        image_urls = []
        
        for field in foli_detail._meta.fields: # generiek voor meerdere foto's
          print(field.name, field.get_internal_type(), type(field))
          if isinstance(field, ImageField):
            image = field.value_from_object(foli_detail)
            if image:
              image_urls.append(image.url)

        print("IMAGE URLS:", image_urls)  # 👈 DEBUG
        context["image_urls"] = image_urls
        return context


       # print(foli_detail)          # laat __str__ zien
       # print(foli_detail.id)       # of andere velden
       # print(foli_detail.afbeeld1) # check of image bestaat
### -- PORTFOLIO -- ### 


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

