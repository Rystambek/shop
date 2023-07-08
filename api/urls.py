from django.urls import path
from .views import ProductView,UserView,OrderView,CommentView,LikeView


urlpatterns = [
    path('product/', ProductView.as_view()),
    path('product/<int:pk>/', ProductView.as_view()),
    path('user/', UserView.as_view()),
    path('user/<int:pk>/', UserView.as_view()),
    path('order/', OrderView.as_view()),
    path('order/<int:pk>/', OrderView.as_view()),
    path('comment/',CommentView.as_view()),
    path('comment/<int:pk>/',CommentView.as_view()),
    path('like/',LikeView.as_view()),
    path('like/<int:pk>/',LikeView.as_view())
]