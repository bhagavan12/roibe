from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

def health_check(request):
    return JsonResponse({'status': 'healthy', 'message': 'ROI Calculator API is running'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', health_check, name='health_check'),
    path('api/', include('users.urls')),
    path('api/', include('results.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
