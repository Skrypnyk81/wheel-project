from django.db import models
from django.utils.text import slugify


class Wheel(models.Model):
    SEASON_CHOICES = [
        ("Tutto", "Tutto"),
        ("Estivi", "Estivi"),
        ("Invernali", "Invernali"),
        ("Per tutte le stagioni", "Per tutte le stagioni"),
    ]
    width = models.IntegerField(null=True, blank=True)
    ratio = models.IntegerField(null=True, blank=True)
    diameter = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    load = models.IntegerField(null=True, blank=True)
    speed = models.CharField(max_length=2, null=True, blank=True)
    season = models.CharField(max_length=50, choices=SEASON_CHOICES, default="Tutto", null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    runflat = models.BooleanField(null=True, blank=True)
    dot = models.IntegerField(null=True, blank=True)
    reinforced = models.BooleanField(null=True, blank=True)
    load_c = models.BooleanField(null=True, blank=True)
    on_sale = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.CharField(max_length=80, blank=False, null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.brand)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.brand)


class WheelsImage(models.Model):
    wheel = models.ForeignKey(Wheel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="wheels")

    def __str__(self):
        return f"{self.wheel}"

class Order(models.Model):
    wheel = models.OneToOneField(Wheel, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    second_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.second_name)
