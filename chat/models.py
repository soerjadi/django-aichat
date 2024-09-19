from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class ChatMessage(models.Model):
    id = models.BigAutoField(primary_key=True)
    sender = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now(), null=True)
