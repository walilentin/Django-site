from django.db import models

from core.models import BaseModel

class Video(BaseModel):
    url = models.URLField(max_length=512)
