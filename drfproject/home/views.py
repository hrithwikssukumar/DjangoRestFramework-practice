from rest_framework.decorators import api_view
from rest_framework.response import Response

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
        return Response('THis is a PUT method')    

    

    