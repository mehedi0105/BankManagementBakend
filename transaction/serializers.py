from rest_framework import serializers
from . import models


class TransactionSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.TransactionHistory
        fields = '__all__'
