from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from datetime import datetime

from .models import *
from .serializers import *

from socket import *
import pickle as pick
from django.contrib.auth import *
from django.http import HttpResponseRedirect

class index(APIView):

    def get(self, request, format = None):
        return render(request, 'adminpage/homepage.html')
    # return HttpResponse("Welcome to Smart IDs admin page.")

class modules(APIView):

    def post(self, request, format = None):
        theUser = authenticate(username = request.data['SN'], password = request.data['pwd'])
        if theUser is not None:
            login(request, theUser)
            if Student.objects.get(user = theUser).user_type == 'prof':
                return HttpResponseRedirect('http://localhost:8000/smartid/studentlist/')
            elif Student.objects.get(user = theUser).user_type == 'student':
                return HttpResponseRedirect('http://localhost:8000/smartid/profcheck/')
            else:
                return Response('Authenticated')
        else:
            return HttpResponseRedirect('http://localhost:8000/smartid/')

class profCheck(APIView):

    def get(self, request, format = None):
        if request.user.is_authenticated():
            userType = Student.objects.get(user = request.user).user_type
            if userType == 'student': 
                payload = {'professors' : Student.objects.filter(user_type = 'prof'), 'user' : Student.objects.get(user = request.user)}
                return render(request, 'adminpage/profcheck.html', payload)
            elif userType == 'prof':
                return HttpResponseRedirect('http://localhost:8000/smartid/studentlist/')
        else:
            return HttpResponseRedirect('http://localhost:8000/smartid/')            

class myData(APIView):

    def get(self, request, format = None):
        return Response('ProfPage')

class studentList(APIView):

    def get(self, request, format = None):
        if request.user.is_authenticated():
            userType = Student.objects.get(user = request.user).user_type
            if userType == 'prof': 
                payload = {'students' : Student.objects.filter(user_type = 'student'), 'user':Student.objects.get(user = request.user)}
                return render(request, 'adminpage/studentlist.html', payload)
            elif userType == 'student':
                return HttpResponseRedirect('http://localhost:8000/smartid/profcheck/')
        else:
            return HttpResponseRedirect('http://localhost:8000/smartid/')            

class professorList(APIView):

    def post(self, request, format = None):
        return Response('ProfPage')

class addUser(APIView):

    def post(self, request, format = None):
        return Response('ProfPage')

class timeInOut(APIView):

    def post(self, request, format = None):
        serializer = timeSerializer(data = request.data)
        if serializer.is_valid():
            serTime = serializer.data["time"]
            serSN = serializer.data["studentNumber"]
            try:
                studentObj = Student.objects.get(student_number = serSN)
                print(serTime)
                if studentObj.inTheBldg:
                    timeQS = timeOut(timestamp = datetime.strptime(serTime, '%m/%d/%y %I:%M:%S %p'), student = studentObj)
                    timeQS.save()
                    studentObj.inTheBldg = False
                    studentObj.save()
                    return Response({"studentNumber": serSN, "inTheBldg": False, "firstName": studentObj.first_name}, status=status.HTTP_201_CREATED)
                else:
                    timeQS = timeIn(timestamp = datetime.strptime(serTime, '%m/%d/%y %I:%M:%S %p'), student = studentObj)
                    timeQS.save()
                    studentObj.inTheBldg = True
                    studentObj.save() 
                    return Response({"studentNumber": serSN, "inTheBldg": True, "firstName": studentObj.first_name}, status=status.HTTP_201_CREATED)
            except Student.DoesNotExist:
                    return Response({"error": "SN does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class writerfid(APIView):

    def get(self, request, format = None):

        # Send to Reader which contacts the Arduino
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect(('localhost',5000))
        clientSocket.send(request.query_params['student_number'].encode('UTF-8'))
        ACK = clientSocket.recv(1024)
        clientSocket.close()

        #Save to Database
        # newUser = Student()

        return Response(request.query_params, status=status.HTTP_201_CREATED);
