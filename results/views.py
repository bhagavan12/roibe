from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse
import csv
import json
from .models import Result
from .serializers import ResultSerializer, ResultCreateSerializer


class ResultListCreateView(generics.ListCreateAPIView):
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Result.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ResultDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Result.objects.filter(user=self.request.user)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def export_results(request):
    results = Result.objects.filter(user=request.user)
    
    # Create CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="roi_calculations.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['ID', 'Timestamp', 'Type', 'Inputs', 'Results'])
    
    for result in results:
        writer.writerow([
            result.id,
            result.timestamp.isoformat(),
            result.type,
            json.dumps(result.inputs),
            json.dumps(result.results)
        ])
    
    return response
