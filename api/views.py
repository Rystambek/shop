from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request


from .models import Product, Order,Comment,Like,User
from .serializers import ProductSerializer, UserSerializer,OrderSerializer, CommentSerializer, LikeSerializer

class ProductView(APIView):
    def get(self, request: Request, pk=None)->Response:
        if pk is None:
            product =Product.objects.all()
            serializer = ProductSerializer(product, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)        
    def post(self, request: Request) -> Response:
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request: Request, pk) -> Response:
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request: Request, pk) -> Response:
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer.delete()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    def get(self, request: Request, pk=None)->Response:
        if pk is None:
            users =User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request: Request, pk) -> Response:
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request: Request, pk) -> Response:
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    
class OrderView(APIView):
    def get(self, request: Request, pk=None) -> Response:
        if pk is None:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            order = Order.objects.get(pk=pk)
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request: Request) -> Response:
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request: Request, pk) -> Response:
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request: Request, pk) -> Response:
        try:
            order = Order.objects.get(pk=pk)
            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class CommentView(APIView):
    def get(self, request: Request, pk=None) -> Response:
        if pk is None:
            comments = Comment.objects.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def post(self, request: Request) -> Response:
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request: Request, pk) -> Response:
        try:
            comment = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request: Request, pk) -> Response:
        try:
            comment = Comment.objects.get(pk=pk)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class LikeView(APIView):
    def get(self, request: Request, pk=None) -> Response:
        if pk is None:
            likes = Like.objects.all()
            serializer = LikeSerializer(likes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            like = Like.objects.get(pk=pk)
            serializer = LikeSerializer(like)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def post(self, request: Request) -> Response:
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request: Request, pk) -> Response:
        try:
            like = Like.objects.get(pk=pk)
        except Like.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = LikeSerializer(like, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request: Request, pk) -> Response:
        try:
            like = Like.objects.get(pk=pk)
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)