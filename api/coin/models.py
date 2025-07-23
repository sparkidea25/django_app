from django.db import models

# Create your models here.
from django.db import models

class Coin(models.Model):
    name = models.CharField(max_length=200)
    contract_address = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        indexes = [models.Index(fields=['name', 'contract_address','instructions'])]

