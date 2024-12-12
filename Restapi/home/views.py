from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def index(request):

    person_details = {
        'name':'Hrithwik',
        'age ':28,
        'job': 'software developer'
    }
    return Response(person_details)