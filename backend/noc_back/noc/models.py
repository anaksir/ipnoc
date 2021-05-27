from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Region(models.Model):
    short_name = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50)


class Device(models.Model):

    class Status(models.TextChoices):
        ACTIVE = 'active'
        INACTIVE = 'inactive'

    class Role(models.TextChoices):
        SWITCH = 'switch'
        ROUTER = 'router'

    hostname = models.CharField(
        max_length=6,
        unique=True,
    )

    ip_address = models.GenericIPAddressField(
        protocol='IPv4',
        unique=True,
    )

    status = models.CharField(
        max_length=8,
        choices=Status.choices,
        default=Status.ACTIVE,
    )

    role = models.CharField(
        max_length=6,
        choices=Role.choices,
    )

    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class Client(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )


class Order(models.Model):
    order_id = models.CharField(max_length=12, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


class Interface(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    phy_int = models.CharField(max_length=20)
    vlan = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(100), MaxValueValidator(3999)],
    )
