from django.db import models

# Create your models here.
# models.py

class Rubrique(models.Model):
    titre = models.CharField(max_length=100),
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.titre
