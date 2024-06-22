from django.urls import path
from . views import homepageview , aboutpageiew

urlpatterns = [
    path('',homepageview.as_view(), name='home'),
    path('about/', aboutpageiew.as_view(), name='about'),
]