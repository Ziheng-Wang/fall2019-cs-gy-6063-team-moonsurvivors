from django.db import models


class SimulatedData(models.Model):
    """This model represents the sensors that we expect to
    potentially available in the future in the NYU Motorsports
    Racing vehicle."""

    created_at = models.DateTimeField()

    # Oil temperature panel, measured in fahrenheit
    temperature = models.FloatField(default=0)

    # Acceleration Panel, measured in meter/second
    acceleration_x = models.FloatField(default=0)
    acceleration_y = models.FloatField(default=0)
    acceleration_z = models.FloatField(default=0)

    # Wheel Speed Panel for each of the four wheels
    # measured in meter/second
    wheel_speed_fr = models.FloatField(default=0)
    wheel_speed_fl = models.FloatField(default=0)
    wheel_speed_br = models.FloatField(default=0)
    wheel_speed_bl = models.FloatField(default=0)

    # Suspension/Compression Panel for each of the four wheels
    # measured in centimeter
    suspension_fr = models.FloatField(default=0)
    suspension_fl = models.FloatField(default=0)
    suspension_br = models.FloatField(default=0)
    suspension_bl = models.FloatField(default=0)

    # Fuel Supply Panel
    # measured in liters
    current_fuel_level = models.FloatField(default=0)
