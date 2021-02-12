from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

class Youtube(APIView):
    def get(self,request,format = None):
        return Response({"pesan":"ini jalan"})

def home(request):
    return HttpResponse("<h1>hai world</h1>")