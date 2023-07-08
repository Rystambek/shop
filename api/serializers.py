from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product,Order,Comment,Like



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields =['id','username','password']
class OrderSerializer(serializers.ModelSerializer):
    # product = ProductSerializer(read_only=True)
    # user = UserSerializer(read_only=True)
    class Meta:
        model=Order
        fields = "__all__" #['id','user','product']
class CommentSerializer(serializers.ModelSerializer):
    # product = ProductSerializer(read_only=True)
    # user = UserSerializer(read_only=True)
    class Meta:
        model=Comment
        fields = "__all__" #['id','text','user','product']
class LikeSerializer(serializers.ModelSerializer):
    # product = ProductSerializer( read_only=True)
    # user = UserSerializer(read_only=True)
    class Meta:
        model=Like
        fields = "__all__" #['id','like','user','product']
