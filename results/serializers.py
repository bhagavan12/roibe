from rest_framework import serializers
from .models import Result


class ResultSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = Result
        fields = ['id', 'user', 'timestamp', 'type', 'inputs', 'results']
        read_only_fields = ['id', 'user', 'timestamp']


class ResultCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['type', 'inputs', 'results']
