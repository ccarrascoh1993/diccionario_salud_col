from django.db import models

class Termino(models.Model):
    term = models.CharField(max_length=100)
    definition = models.TextField()

    def __str__(self):
        return self.term