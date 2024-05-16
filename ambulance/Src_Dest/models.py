from django.db import models

# Create your models here.
class data(models.Model):
    source = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)

    # def __str__(self):
    #     return self.title
