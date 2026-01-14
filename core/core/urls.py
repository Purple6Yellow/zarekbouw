from django.contrib import admin
from django.urls import path, include
from App_zarek.views import index_view

urlpatterns = [
    path('', index_view), 
    path('admin/', admin.site.urls),
    path('', include ('App_zarek.urls')),

]

