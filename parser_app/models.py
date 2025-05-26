from django.db import models

class Parser_Kinob(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title