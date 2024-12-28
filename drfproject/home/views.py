from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializer import PersonSerializer

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
            return Response({"error": "Person not found"}, status=404)  # HTTP 404 for not found
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

    
  


    




            

    

    