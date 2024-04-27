from django.db import models

class Link(models.Model):
    content = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.content
