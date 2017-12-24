from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import JSONField



class GeneralRisk(models.Model):
    riskName = models.CharField(max_length=20)
    attr = JSONField()

    def __str__(self):
        return self.riskName