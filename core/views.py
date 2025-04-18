from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import QueryLog
from .utils import get_tone_intent_and_suggestions
from .serializers import AnalyzeRequestSerializer

@api_view(['POST'])
def analyze_query(request):
    serializer = AnalyzeRequestSerializer(data=request.data)
    if serializer.is_valid():
        query = serializer.validated_data['query']
        tone, intent, suggestions = get_tone_intent_and_suggestions(query)

        QueryLog.objects.create(
            query=query,
            tone=tone,
            intent=intent,
            suggested_actions=suggestions
        )

        return Response({
            "query": query,
            "analysis": {"tone": tone, "intent": intent},
            "suggested_actions": suggestions
        })
    return Response(serializer.errors, status=400)