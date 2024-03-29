from rest_framework.response import Response
from rest_framework import generics
from library.models import Book, CartItem, Cart
from library.serializers import BookSerializer, CartItemSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('category', 'level')


class BookRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AddToCartView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]


class ViewCartView(generics.ListAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cart = Cart.objects.get(user=self.request.user)
        return cart.items.all()

