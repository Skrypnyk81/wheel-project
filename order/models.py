from django.db import models
from django.utils.text import slugify


class Wheel(models.Model):
    SEASON_CHOICES = [
        ("Estivi", "Estivi"),
        ("Invernali", "Invernali"),
        ("Per tutte le stagioni", "Per tutte le stagioni"),
    ]
    width = models.IntegerField(verbose_name="Larghezza", null=True, blank=True)
    ratio = models.IntegerField(verbose_name="Altezza", null=True, blank=True)
    diameter = models.IntegerField(verbose_name="Diametro", null=True, blank=True)
    load = models.IntegerField(verbose_name="Carico", null=True, blank=True)
    speed = models.CharField(verbose_name="Velocità", max_length=2, null=True, blank=True)
    season = models.CharField(verbose_name="Stagione", max_length=50, choices=SEASON_CHOICES, default="Invernali",
                              null=True, blank=True)
    tread = models.IntegerField(verbose_name="Battistrada", null=True, blank=True)
    brand = models.CharField(verbose_name="Marca", max_length=50, null=True, blank=True)
    quantity = models.CharField(verbose_name="Quantità", max_length=50, null=True, blank=True)
    dot = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(verbose_name="Prezzo", max_digits=7, decimal_places=2, null=True, blank=True)
    on_sale = models.BooleanField(verbose_name="In vendita", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return str(self.brand)


class WheelsImage(models.Model):
    wheel = models.ForeignKey(Wheel, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="wheels")

    def __str__(self):
        return f"{self.wheel}"


class Order(models.Model):
    wheel = models.OneToOneField(Wheel, on_delete=models.DO_NOTHING, related_name="order")
    first_name = models.CharField(verbose_name="Nome", max_length=20, null=True, blank=True)
    second_name = models.CharField(verbose_name="Cognome", max_length=50, null=True, blank=True)
    phone = models.CharField(verbose_name="Telefono", max_length=200, null=True, blank=True)
    street = models.CharField(verbose_name="Via", max_length=255, null=True, blank=True)
    city = models.CharField(verbose_name="Città", max_length=100, null=True, blank=True)
    state = models.CharField(verbose_name="Provincia", max_length=100, null=True, blank=True)
    postal_code = models.CharField(verbose_name="CAP", max_length=10, null=True, blank=True)
    email = models.EmailField(verbose_name="Email", max_length=254, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.second_name)
