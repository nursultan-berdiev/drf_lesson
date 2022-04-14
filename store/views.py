from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, \
    ListModelMixin

from rest_framework.viewsets import ViewSet

from .serializers import CategorySerializer, BookSerializer
from .models import Category, Book


class CategoryAPIView(GenericViewSet, ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin,
                      RetrieveModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class CategoryCreateAPIView(CreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class CategoryListAPIView(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookAPIViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
