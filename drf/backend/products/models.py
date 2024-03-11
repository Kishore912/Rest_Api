from django.db import models

# Create your models here.
class products(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits = 50 , decimal_places=2,default=99.99)
