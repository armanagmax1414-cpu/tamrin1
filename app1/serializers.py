from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Mahsol,Market,Camment,Like,CartItem

class Cammentserializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)

    class Meta:
        model=Camment
        fields=['id','user','text','mahsol','created_at']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Like
        fields=['id','user','mahsol','created_at']
        read_only_fields=['user']                        
class MahsolSerializer(serializers.ModelSerializer):
    author=serializers.StringRelatedField(read_only=True)
    total_likes=serializers.IntegerField(source='total_like',read_only=True)
    camments=Cammentserializer(many=True,read_only=True)
    class Meta:
        model=Mahsol
        fields='__all__'


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model=Market
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['id', 'name', 'price', 'inventory'] 

