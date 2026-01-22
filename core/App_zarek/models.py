from django.db import models
from PIL import Image
from django.utils import timezone

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
  afbeeld3 = models.ImageField(upload_to='avatars/', null=True, blank = True)
  afbeeld4 = models.ImageField(upload_to='avatars/', null=True, blank = True)
  afbeeld5 = models.ImageField(upload_to='avatars/', null=True, blank = True)
  afbeeld6 = models.ImageField(upload_to='avatars/', null=True, blank = True)
  created_by = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return str(self.naam)
  
  def get_absolute_url(self):
        return reverse("DetailFoli_url", kwargs={"pk": self.pk})
#### // FOTOPORTFOLIOR### 