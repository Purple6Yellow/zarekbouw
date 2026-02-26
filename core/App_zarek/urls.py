from . import views
from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import set_language

urlpatterns = [
    ### DEFENITIEF### 

    path('index.html/', index_view),    
    path('diensten.html/', diensten_view),
    path('contact.html/', contact_view), 
    path('test.html/', test_view),
    path('hulpcontact.html/', hulpcontact_view), 

    path('portfolio.html/', FoliListView.as_view(), name = 'OverzichtFoli_url'),
    path("portfolio_detail.html/<int:pk>/", DetailFoli.as_view(), name="DetailFoli_url"),  # detailpagina
 
### // KUNST -- ### 
    path("i18n/setlang/", set_language, name = "set_language"), #internationale vertaling

    path("index.html/", FoliCardView.as_view(), name="CardFoli.url"),

]

if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL, document_root  =settings.MEDIA_ROOT)