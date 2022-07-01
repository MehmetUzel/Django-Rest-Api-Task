from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
from forex_python.converter import CurrencyRates


class CurrencyViews(APIView):
    def get(self, request):
        if True:
            c = CurrencyRates()
            rate = c.get_rate('USD', 'EUR')
            return Response({"status": "success", "data": rate}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": "not welcome"}, status=status.HTTP_400_BAD_REQUEST)

class IpViews(APIView):
    def get(self, request):
        if True:
            externalIP  = os.popen('curl -s ifconfig.me').readline()
            return Response({"status": "success", "data": externalIP}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": "not welcome"}, status=status.HTTP_400_BAD_REQUEST)
