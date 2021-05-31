from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Vendor(models.Model):
    name = models.CharField(max_length=20, unique=True)


class Software(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True)


class Model(models.Model):
    name = models.CharField(max_length=20, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    software = models.ForeignKey(Software, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.vendor.name} {self.name}'


class Region(models.Model):
    short_name = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}({self.short_name})'


class Device(models.Model):

    class Status(models.TextChoices):
        ACTIVE = 'active'
        INACTIVE = 'inactive'

    class Role(models.TextChoices):
        SWITCH = 'switch'
        ROUTER = 'router'

    hostname = models.CharField(
        max_length=7,
        unique=True,
    )

    ip_address = models.GenericIPAddressField(
        protocol='IPv4',
        unique=True,
    )

    model = models.ForeignKey(Model, on_delete=models.CASCADE)

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

    def __str__(self):
        return f'{self.role} {self.hostname}({self.ip_address})'


class Client(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    email = models.EmailField()
    region = models.ManyToManyField(Region)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    order_id = models.CharField(max_length=12, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.order_id}'


class Interface(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    phy_int = models.CharField(max_length=20)
    vlan = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(100), MaxValueValidator(3999)],
    )

    def __str__(self):
        return f'{self.device} {self.phy_int}.{self.vlan}'
