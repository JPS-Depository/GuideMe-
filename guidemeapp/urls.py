from django.urls import path

from .views import *

urlpatterns =[
    path('',Index, name='index'),
    path('homepage/', HomePage, name='homepage'),
    path('tour_guide/', TourGuide, name='tour_guide'),
    path('tour_guide/list_guide', ListGuide, name='list_guide'),
    path('tour_guide/list_guide/profile_guide', ProfileGuide, name='profile_guide'),
    path('lokasi/', LokasiTour, name='lokasi'),
    path('pesanan/', PesananList, name='pesanan')

]