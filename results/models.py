from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Result(models.Model):
    CALCULATION_TYPES = [
        ('quick', 'Quick'),
        ('full', 'Full'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='results')
    timestamp = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=CALCULATION_TYPES)
    inputs = models.JSONField()
    results = models.JSONField()
    
    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.user.email} - {self.type} calculation - {self.timestamp}"
