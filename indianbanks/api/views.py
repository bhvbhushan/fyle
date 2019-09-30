from django.shortcuts import render
from rest_framework import generics
from .models import BankBranches
from .serializers import BankSerializer

from rest_framework.response import Response
from rest_framework.views import status

# Create your views here.

class ListBankView(generics.ListAPIView):
    queryset = BankBranches.objects.all()
    serializer_class = BankSerializer

class IFSCBankSearch(generics.RetrieveAPIView):
    queryset = BankBranches.objects.all()
    serializer_class = BankSerializer

    def get(self, request, *args, **kwargs):
        try:
            bank = self.queryset.get(pk=kwargs["pk"])
            return Response(BankSerializer(bank).data)
        except BankBranches.DoesNotExist:
            return Response(
                data = {
                    "message": "Bank with IFSC Code: {} does not exist".format(kwargs["pk"])
                },
                status = status.HTTP_404_NOT_FOUND
            )

class CityOrNameBankSearch(generics.ListAPIView):
    queryset = BankBranches.objects.all()
    serializer_class = BankSerializer
    filterset_fields = ['city', 'bank_name']