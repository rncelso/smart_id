from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from datetime import datetime

from .models import *
from .serializers import *

def index(request):
    return HttpResponse("Welcome to Smart IDs admin page.")

class timeInOut(APIView):

    def post(self, request, format = None):
        serializer = timeSerializer(data = request.data)
        if serializer.is_valid():
            serTime = serializer.data["time"]
            serSN = serializer.data["studentNumber"]
            studentObj = Student.objects.get(student_number = serSN)
            print(serTime)
            if studentObj.inTheBldg:
                timeQS = timeOut(timestamp = datetime.strptime(serTime, '%m/%d/%y %I:%M:%S %p'), student = studentObj)
                timeQS.save()
                studentObj.inTheBldg = False
                studentObj.save() 
            else:
                timeQS = timeIn(timestamp = datetime.strptime(serTime, '%m/%d/%y %I:%M:%S %p'), student = studentObj)
                timeQS.save()
                studentObj.inTheBldg = True
                studentObj.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
