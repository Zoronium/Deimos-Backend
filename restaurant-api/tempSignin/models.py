from django.db import models
from django.utils import timezone
import uuid


# Create your models here.
class tempUser(models.Model):
    name = models.CharField(max_length=255)
    Uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    email = models.EmailField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    expiration = models.DateTimeField(
        default=timezone.now() + timezone.timedelta(minutes=15)
    )

    def __str__(self):
        return str(self.name) + str(self.expiration)
