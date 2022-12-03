from django.db import models

# Create your models here.
class Kimlik(models.Model):
    id=models.IntegerField(primary_key=True)
    Ad=models.CharField(max_length=500)
    Soyad=models.CharField(max_length=500)
def __str__(self):
    return self.Ad