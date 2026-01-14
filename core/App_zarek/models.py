from django.db import models
from PIL import Image

####### INVOEGEN VIA FORMS.PY
#### CONTACTFORMULIER###
class Contact (models.Model):
  naam = models.CharField(max_length =100)
  email = models.EmailField()
  bericht = models.CharField(max_length = 500)

  def __str__(self):
    return str(self.naam) + " (" + str(self.email)  +")"
#### // CONTACTFORMULIER###

####### INVOEGEN VIA ADMIN OMGEVING


#### FOTOPORTFOLIO###
class Portfolio (models.Model):
  naam = models.CharField(max_length =100)
  afbeeld1 = models.ImageField(upload_to='avatars/', null=True, blank = True)
  afbeeld2 = models.ImageField(upload_to='avatars/', null=True, blank = True)

  def __str__(self):
    return str(self.naam)
#### // FOTOPORTFOLIOR###