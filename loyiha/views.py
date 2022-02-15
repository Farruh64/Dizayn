from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
class IshchiViewSet(viewsets.ModelViewSet):
    queryset = Ishchi.objects.all()
    serializer_class = IshchiSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated, DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['ismi','familiyasi']
    search_fields = ['ismi','familiyasi']
    ordering_fields = ['ismi']
    ordering = ['id']


class LoyihaViewSet(viewsets.ModelViewSet):
    queryset = Loyiha.objects.all()
    serializer_class = LoyihaSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['nomi']
    search_fields = ['nomi']
    ordering_fields = ['nomi']
    ordering = ['id']


class KategoriyaViewSet(viewsets.ModelViewSet):
    queryset = Kategoriya.objects.all()
    serializer_class = KategoriyaSerializer 
# Create your views here.
