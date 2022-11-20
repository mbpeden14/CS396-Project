from django.db import models

# Create your models here.

class MyFileUpload(models.Model):
    name=models.CharField(max_length=50)
    file=models.FileField()

    class Meta:
        verbose_name = "File Upload"