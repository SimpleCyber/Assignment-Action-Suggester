from django.urls import path
from .views import analyze_query

urlpatterns = [
    path('api/analyze/', analyze_query),
]