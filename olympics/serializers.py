from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__' # fields = ['event_key', 'name', 'sex', 'age', 'height', 'weight', 'team', 'noc', 'games', 'year', 'season', 'city', 'sport', 'event', 'medal']