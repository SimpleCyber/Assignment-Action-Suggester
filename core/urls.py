from django.urls import path
from .views import analyze_query, home

urlpatterns = [
    path('api/analyze/', analyze_query),
    path('', home, name='home'),
]