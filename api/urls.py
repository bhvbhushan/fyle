from django.urls import path
from .views import ListBankView, IFSCBankSearch, CityOrNameBankSearch

urlpatterns = [
    path('bank/', ListBankView.as_view(), name='banks-all'),
    path('bank_ifsc/', IFSCBankSearch.as_view(), name='ifsc-detail'),
    path(r'city_bank/', CityOrNameBankSearch.as_view(), name='city-or-name-detail')
]