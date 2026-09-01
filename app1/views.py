

from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import MahsolSerializer,MarketSerializer,Cammentserializer,LikeSerializer
from .models import Mahsol,Market,Like,Camment
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
class  MahsolList2(generics.ListAPIView):
    queryset=Mahsol.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=MahsolSerializer

    def perform_create(self,serializer):
        serializer.save(author=self.request.user)

class ToggleLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def mahsol(self, request, Mahsol_id):
        mahsol = get_object_or_404(Mahsol, id=Mahsol_id)
        user = request.user

        like, created = Like.objects.get_or_create(user=user, mahsol=mahsol)

        if created:
            return Response({"message": "Like"}, status=status.HTTP_201_CREATED)
        else:
            like.delete()
            return Response({"message": "onLike"}, status=status.HTTP_200_OK)
class CreatCammentView(generics.CreateAPIView):
    serializer_class=Cammentserializer
    permission_classes=[IsAuthenticated]

    def created(self,request,*args,**kwargs):
        mahsol_id=self.kwargs['mahsol_id']
        mahsol=get_object_or_404(mahsol,id=mahsol_id)

        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exeption=True)
        serializer.save(user=request.user,mahsol=mahsol)

        return Response({
            "message":"camment",
            "mahsol_id":mahsol_id,
            "data":serializer.data,
        },status=status.HTTP_201_CREATED)
   
class MahsolListAPIView(generics.ListAPIView):
    queryset=Mahsol.objects.all()
    serializer_class=MahsolSerializer

class MahsolDetailAPIView(generics.RetrieveAPIView):
    queryset=Mahsol.objects.all()
    serializer_class=MahsolSerializer
    lookup_field="pk"

class MarketListAPIView(generics.ListAPIView):
    queryset=Mahsol.objects.all()
    serializer_class=MarketSerializer    


class MarketDetailAPIview(generics.RetrieveAPIView):
    queryset=Market.objects.all()
    serializer_class=MarketSerializer
    lookup_field="pk"



class MahsolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset =Mahsol.objects.all()
    serializer_class =MahsolSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 

from .serializers import MahsolSerializer,MarketSerializer
from .models import Mahsol,Market
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

User = get_user_model()

class MahsolViewSet(viewsets.ModelViewSet):
    queryset=Mahsol.objects.all()
    serializer_class=MahsolSerializer


class MarketViewSet(viewsets.ModelViewSet):
    queryset=Market.objects.all()
    serializer_class=MarketSerializer    
