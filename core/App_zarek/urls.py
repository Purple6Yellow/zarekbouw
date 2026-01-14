from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import set_language

urlpatterns = [
    ### DEFENITIEF### 
    path('index.html/', index_view),
    path('contact.html/', contact_view),
    path('portfolio.html/', foli),
    path('portfolio.html/', OverzichtFoli.as_view(), name = 'OverzichtFoli_url'),
    path('portfolio_detail.html/<int:pk>/', DetailFoli.as_view(), name = 'DetailFoli_url'),
### // KUNST -- ### 
    path("i18n/setlang/", set_language, name = "set_language"), #internationale vertaling

]

if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL, document_root  =settings.MEDIA_ROOT)