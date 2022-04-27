from django.db import models

from django.core.validators import FileExtensionValidator

class DataInput(models.Model):
    upload = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['csv'])])
    filling = models.CharField(max_length=80, blank=True)