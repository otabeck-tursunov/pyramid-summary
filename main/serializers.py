import json

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Person, Status


class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'status', 'score', 'connection', 'stage', 'person')
        read_only_fields = ('connection', 'stage')

    def create(self, validated_data):
        person = Person.objects.create(
            name=validated_data['name'],
            score=validated_data['score'],
            person=validated_data['person'],
            status=validated_data['status'],
            stage=1,
            connection=None
        )
        person.connection = {
            person.id: validated_data.get('status').name
        }
        if person.person is not None:
            connection = person.person.connection
            connection.update(person.connection)
            person.connection = connection
            person.stage = person.person.stage + 1
        elif len(Person.objects.all()) > 1:
            person.delete()
            raise serializers.ValidationError('Referal belgilanmagan!')
        person.save()
        return person
