from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    image_url = models.CharField(max_length=100)
    image_alt = models.CharField(max_length=500)
    source_code_url = models.CharField(max_length=1000)
    live_url = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name
