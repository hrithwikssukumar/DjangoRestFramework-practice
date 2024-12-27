from rest_framework import serializers
from home.models import Person

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        name = Person
        fields ='__all__'