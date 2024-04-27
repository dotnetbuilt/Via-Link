from django.db import models

class Link(models.Model):
    content = models.CharField(max_length=500)
    title = models.CharField(max_length=150, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
