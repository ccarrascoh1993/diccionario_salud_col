from django.db import models

class Termino(models.Model):
    termino = models.CharField(max_length=100)
    definicion = models.TextField()

    def __str__(self):
        return self.term