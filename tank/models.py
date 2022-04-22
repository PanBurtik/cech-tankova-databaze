from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Nationality(models.Model):
    name = models.CharField(max_length=50, verbose_name="Jméno státu:")

    fullname = models.CharField(max_length=50, verbose_name="Celý název:")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Tank(models.Model):
    name = models.CharField(max_length=50, verbose_name="Název tanku:")

    description = models.TextField(verbose_name="Popis tanku:")

    TYPE = (
        ("light", "Lehký tank"),
        ("medium","Střední tank"),
        ("heavy", "Těžký tank"),
        ("td", "stíhač tanků"),
        ("arty", "Dělostřelectvo")
    )

    type = models.CharField(max_length=50, choices = TYPE,verbose_name="Typ vozidla:", help_text="Vyberte typ vozidla")

    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, verbose_name="Stát:")

    PRESENCE = (
        ("1.", "V 1. světové válce"),
        ("2.", "V 2. světové válce"),
        ("3.", "V jiné"),
        ("0.", "V žádné")
    )

    pressence = models.CharField(max_length=50, choices=PRESENCE, verbose_name="Výskyt:", help_text="Vyberte období, ve kterém se vozidlo vyskytovalo")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Maker(models.Model):
    name = models.CharField(max_length=50, verbose_name="Jméno/název várobce:")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Characteristics(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE, verbose_name="Výrobce:")

    CREW = (
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6")
    )

    crew = models.CharField(max_length=1, choices=CREW, verbose_name="Členové posádky:", help_text="Vyberte počet členů posádky")

    length = models.DecimalField(decimal_places=2, max_digits=4, verbose_name="Délka vozidla:", help_text="Vepište délku vozidla (v metrech)")

    width = models.DecimalField(decimal_places=2, max_digits=3, verbose_name="Šířka vozidla:", help_text="Vepište šířku vozidla (v metrech)")

    height = models.DecimalField(decimal_places=2, max_digits=3, verbose_name="Výška vozidla:", help_text="Vepište výšku vozidla (v metrech)")

    mass = models.IntegerField(validators=[MaxValueValidator(250)], verbose_name="Váha vozidla:", help_text="Vepište váhu vozidla (v tunách)")

    tank = models.ForeignKey(Tank, on_delete=models.CASCADE, verbose_name="Tank:")

    class Meta:
        ordering = ['tank']

    def __str__(self):
        return str(self.tank)


class Motor(models.Model):
    name = models.CharField(max_length=50, verbose_name="Název motoru:")

    cylinders = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(14)], verbose_name="Počet válců:")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Movement(models.Model):
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE, verbose_name="Motor:")

    range = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)],verbose_name="Maximální dojezd:", help_text="Vepište maximální dojezd vozidla (V kilometrech)")

    maxspeed = models.IntegerField(validators=[MinValueValidator(0.1), MaxValueValidator(150)],verbose_name="Maximální rychlost", help_text="Vepište maximální rychlost vozidla (V kilometrech za hodinu)")

    tank = models.ForeignKey(Tank, on_delete=models.CASCADE, verbose_name="Tank:")

    class Meta:
        ordering = ['tank']

    def __str__(self):
        return str(self.tank)