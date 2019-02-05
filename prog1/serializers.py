from rest_framework import serializers


class PersonSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    # inn = serializers.IntegerField(required=False)
    # inn = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    surname = serializers.CharField()


class Person1Serializer(serializers.Serializer):

    name = serializers.CharField()
    surname = serializers.CharField()
    age = serializers.IntegerField()

