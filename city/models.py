from django.db import models
from iranian_cities.fields import OstanField

class TestModel(models.Model):
    ostan = OstanField()