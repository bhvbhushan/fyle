from rest_framework import serializers
from .models import BankBranches

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankBranches
        fields = ('__all__')