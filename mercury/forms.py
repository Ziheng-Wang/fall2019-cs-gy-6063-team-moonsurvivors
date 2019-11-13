from django import forms
from mercury.models import TemperatureSensor, AccelerationSensor,WheelSpeedSensor,SuspensionSensor, FuelLevelSensor

# for our slider
from django.forms.widgets import NumberInput


class RangeInput(NumberInput):
    input_type = "range"


class TemperatureForm(forms.ModelForm):
    class Meta:
        model = TemperatureSensor
        fields = "__all__"
        widgets = {
            "temperature": forms.NumberInput(
                attrs={"id": "post-temperature", "required": True}
            ),
            "created_at": forms.DateTimeInput(
                            attrs={"id": "post-created-at", "required": True}
                        )
        }

class AccelerationForm(forms.ModelForm):
    class Meta:
        model = AccelerationSensor
        fields = "__all__"
        widgets = {
            "created_at_accel": forms.DateTimeInput(
                            attrs={"id": "post-created-at_accel", "required": True}
                        ),
            "acceleration_x": forms.NumberInput(
                attrs={"id": "post-acceleration-X", "required": True}
            ),
            "acceleration_y": forms.NumberInput(
                attrs={"id": "post-acceleration-Y", "required": True}
            ),
            "acceleration_z": forms.NumberInput(
                attrs={"id": "post-acceleration-Z", "required": True}
            )
        }

class WheelSpeedForm(forms.ModelForm):
    class Meta:
        model = WheelSpeedSensor
        fields = "__all__"
        widgets = {
            "created_at_ws": forms.DateTimeInput(
                            attrs={"id": "post-created-at_ws", "required": True}
                        ),
            "wheel_speed_fr": forms.NumberInput(
                attrs={"id": "post-wheel-speed-fr", "required": True}
            ),
            "wheel_speed_fl": forms.NumberInput(
                attrs={"id": "post-wheel-speed-fl", "required": True}
            ),
            "wheel_speed_br": forms.NumberInput(
                attrs={"id": "post-wheel-speed-br", "required": True}
            ),
            "wheel_speed_bl": forms.NumberInput(
                attrs={"id": "post-wheel-speed-bl", "required": True}
            )
        }

class SuspensionForm(forms.ModelForm):
    class Meta:
        model = SuspensionSensor
        fields = "__all__"
        widgets = {
            "created_at_ss": forms.DateTimeInput(
                            attrs={"id": "post-created-at_ss", "required": True}
                        ),
            "suspension_fr": forms.NumberInput(
                attrs={"id": "post-suspension-fr", "required": True}
            ),
            "suspension_fl": forms.NumberInput(
                attrs={"id": "post-suspension-fl", "required": True}
            ),
            "suspension_br": forms.NumberInput(
                attrs={"id": "post-suspension-br", "required": True}
            ),
            "suspension_bl": forms.NumberInput(
                attrs={"id": "post-suspension-bl", "required": True}
            )
        }


class FuelLevelForm(forms.ModelForm):
    class Meta:
        model = FuelLevelSensor
        fields = "__all__"
        widgets = {
            "created_at_fl": forms.DateTimeInput(
                            attrs={"id": "post-created-at_fl", "required": True}
                        ),
            "current_fuel_level": forms.NumberInput(
                attrs={"id": "post-current-fuel-level", "required": True}
            )
        }


# class SimulatorForm(forms.ModelForm):
#     class Meta:
#         model = SimulatedData
#         fields = "__all__"
#         widgets = {
#             "temperature": forms.NumberInput(
#                 attrs={"id": "post-temperature", "required": True}
#             ),
#             "acceleration_x": forms.NumberInput(
#                 attrs={"id": "post-acceleration-X", "required": True}
#             ),
#             "acceleration_y": forms.NumberInput(
#                 attrs={"id": "post-acceleration-Y", "required": True}
#             ),
#             "acceleration_z": forms.NumberInput(
#                 attrs={"id": "post-acceleration-Z", "required": True}
#             ),
#             "wheel_speed_fr": forms.NumberInput(
#                 attrs={"id": "post-wheel-speed-fr", "required": True}
#             ),
#             "wheel_speed_fl": forms.NumberInput(
#                 attrs={"id": "post-wheel-speed-fl", "required": True}
#             ),
#             "wheel_speed_br": forms.NumberInput(
#                 attrs={"id": "post-wheel-speed-br", "required": True}
#             ),
#             "wheel_speed_bl": forms.NumberInput(
#                 attrs={"id": "post-wheel-speed-bl", "required": True}
#             ),
#             "suspension_fr": forms.NumberInput(
#                 attrs={"id": "post-suspension-fr", "required": True}
#             ),
#             "suspension_fl": forms.NumberInput(
#                 attrs={"id": "post-suspension-fl", "required": True}
#             ),
#             "suspension_br": forms.NumberInput(
#                 attrs={"id": "post-suspension-br", "required": True}
#             ),
#             "suspension_bl": forms.NumberInput(
#                 attrs={"id": "post-suspension-bl", "required": True}
#             ),
#             "current_fuel_level": forms.NumberInput(
#                 attrs={"id": "post-current-fuel-level", "required": True}
#             ),
#             "created_at": forms.DateTimeInput(
#                 attrs={"id": "post-created-at", "required": True}
#             ),
#         }
