from django.contrib import admin
from .models import Result


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'timestamp', 'id')
    list_filter = ('type', 'timestamp', 'user')
    search_fields = ('user__email', 'user__username')
    readonly_fields = ('timestamp',)
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')
