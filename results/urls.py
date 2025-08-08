from django.urls import path
from . import views

urlpatterns = [
    path('results/', views.ResultListCreateView.as_view(), name='result-list-create'),
    path('results/<int:pk>/', views.ResultDetailView.as_view(), name='result-detail'),
    path('results/export/', views.export_results, name='export-results'),
]
