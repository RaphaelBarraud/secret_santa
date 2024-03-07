from rest_framework import serializers
from .models import Participant, Blacklist


class BlacklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blacklist
        fields = ['id', 'blacklisted']


class ParticipantSerializer(serializers.ModelSerializer):
    # Connect to the blacklist serializer
    blacklist = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Participant
        fields = ['id', 'first_name', 'last_name', 'blacklist']