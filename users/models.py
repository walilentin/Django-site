from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    info = models.CharField(max_length=256, blank=True, null=True)

