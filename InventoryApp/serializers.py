from rest_framework import serializers
from .models import *

class AllproductDtls_Serializers(serializers.ModelSerializer):
    
    class Meta:
        model=Products
        fields='__all__'

class SingleProdDtls_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=['pname','pcode','pprice','categoryid']

class category_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
