from rest_framework import serializers
from .models import PlayerScore

class PlayerScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerScore
        fields = ['ip_address', 'moves', 'time_taken', 'created_at']
        read_only_fields = ['created_at']
