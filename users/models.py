from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    street = models.CharField(max_length=40)

    class Meta:
        db_table = 'Address'

    def __str__(self):
        return f"{self.country} {self.street} {self.city}"


class UserRole(models.TextChoices):
    bakalavr = ("b", "B")
    magistr = ("m", "M")
    ph = ("ph", "PH")


class Users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    email = models.EmailField()
    birth_date = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=UserRole.choices, default=UserRole.bakalavr)

    class Meta:
        db_table = 'Users'

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.username} {self.email}"