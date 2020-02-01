from django.db import models

# Create your models here.
class company(models.Model):
    CompanyName = models.CharField(max_length=100)
    POC         = models.CharField(max_length=100)
    CPOC        = models.CharField(max_length=100)
    Remarks     = models.TextField()
    order       = models.AutoField(primary_key=True)
