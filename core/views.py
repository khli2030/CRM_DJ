from django.http import JsonResponse, response
from django.shortcuts import render, redirect
from rest_framework import serializers
# third party import

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.settings import perform_import
from rest_framework.views import APIView
from rest_framework.response import Response
from .serelizer import PostSerializer, LeadSerilezer
from leads.models import Post, Lead
from rest_framework import generics
from rest_framework import mixins

# here is controlling the Transaction to get/post for end user


class TestView(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostCreateAPI(generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

# thie ListCreateAPI has 2 methods GET/POST


class PostListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostGetAPI(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class LeadTestView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        qs = Lead.objects.all()
        lead1 = qs.first()
        serializer = LeadSerilezer(lead1)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):

        serializer = LeadSerilezer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# class TestView(APIView):
#     permission_classes = (IsAuthenticated,)
#     # this module definded for the endpoint APIview

#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.all()
#         serializer_many = PostSerializer(qs, many=True)
#         post = qs.first()
#         serializer1 = PostSerializer(post)
#         return Response(serializer1.data)

#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         # we should validate the data in Post method to insert it in DB correctlly
#         if serializer.is_valid():
#             # this save() to model
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


# def view_test(request):
#     data = {
#         'name': 'ibrahim',
#         'age' : 29
#     }
#     return JsonResponse(data)
