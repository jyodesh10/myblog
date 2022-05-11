from django.db import models

# Create your models here.


class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=256)
    img = models.ImageField(upload_to='images', height_field=None,
                            width_field=None, max_length=100, null=True, blank=True, )

    def __str__(self):
        return self.title
