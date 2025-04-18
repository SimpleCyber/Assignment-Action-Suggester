from rest_framework import serializers

class AnalyzeRequestSerializer(serializers.Serializer):
    query = serializers.CharField()