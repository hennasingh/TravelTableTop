from django.db import models
import uuid

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    complexity = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    year = models.IntegerField(null=True, blank=True)
    playing_time = models.IntegerField(null=True, blank=True)
    max_playing_time = models.IntegerField(null=True, blank=True)
    min_age = models.IntegerField(null=True, blank=True)
    min_players = models.IntegerField(null=True, blank=True)
    max_players = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    thumbnail = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
