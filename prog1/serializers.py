from rest_framework import serializers


class PersonSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    surname = serializers.CharField()
