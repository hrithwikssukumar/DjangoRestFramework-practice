from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializer import PersonSerializer,RegisterSerializer,LoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework import viewsets


class ClassPerson(APIView):
    
    def get(self,request):
        objperson = Person.objects.all()
        serializer = PersonSerializer(objperson,many = True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201) 
        return Response(serializer.errors, status=400)   
        
@api_view(['GET','POST','PUT'])
def index(request):
    if request.method == 'GET':
        person_details ={
        'name' : 'Hrithwik',
        'age'  : '28',
        'job'  : 'Software developer'
        }
        return Response(person_details)

    elif request.method == 'POST':
        return Response('This is a POST method')
    elif request.method =='PUT':
        return Response('This is a PUT method') 


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def person(request):
    if request.method =='GET':
        objperson = Person.objects.all()
        serializer = PersonSerializer(objperson,many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201) 
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        data = request.data
        try:
            obj = Person.objects.get(id=data['id'])
        except Person.DoesNotExist:
            return Response({"error": "Person not found"}, status=404)  
        serializer = PersonSerializer(obj, data=data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'PATCH':
        data = request.data
        try:
            obj = Person.objects.get(id=data['id'])
        except Person.DoesNotExist:
            return Response({"error": "Person not found"}, status=404)
        serializer = PersonSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        data = request.data
        try:
            obj = Person.objects.get(id = data['id'])
        except Person.DoesNotExist:
            raise Http404("Person not found")
        obj.delete()
        return Response({'message': "Your data is deleted"})

    
class PersonViewSets(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()  

    def list(self,request):
        search = request.GET.get("search")
        queryset = self.queryset
        if search:
            queryset =queryset.filter(name__startswith =search)
        serializer = PersonSerializer(queryset,many=True)
        return Response({'status':200,'data':serializer.data})    



class RegisterAPI(APIView):

    def post(self,request):
        _data = request.data 
        serializer = RegisterSerializer(data=_data)

        if not serializer.is_valid():
            return Response({'message':serializer.errors},status=status.HTTP_404_NOT_FOUND)
        serializer.save()
        return Response({'message':'User created'},status=status.HTTP_201_CREATED)  


class LoginAPI(APIView):

    def post(self,request):
        _data = request.data
        serializer = LoginSerializer(data=_data)

        if not serializer.is_valid():
            return Response({'message':serializer.errors},status=status.HTTP_404_NOT_FOUND)

        user = authenticate(
        username=serializer.validated_data['username'], 
        password=serializer.validated_data['password']
        )
       
        if not user:
            return Response({'message':"Invalid credentials"},status=status.HTTP_404_NOT_FOUND)

        token,_ = Token.objects.get_or_create(user=user)
        return Response({"message":"Login Successful",'token':str(token)},status=status.HTTP_201_CREATED)
        



    




            

    

    