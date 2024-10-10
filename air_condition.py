from logging import raiseExceptions
from operator import truediv


class Air_Condition:

    def __init__(self):
        self.is_on: bool = False
        self.temperature: int = 16
        self.fan_speed: int = 1

    def ac_is_off(self):
        self.is_on = False

    def turn_on_ac(self):
        self.is_on = True

    def ac_is_on(self):
        return self.is_on

    def increase_temperature(self):
        if self.is_on:
            if self.temperature  < 30:
                self.temperature += 1
            else:
                self.temperature = 30

    def decrease_temperature(self):
        if self.is_on:
            if self.temperature > 16:
                self.temperature -= 1
            else:
                self.temperature = 16

    def get_temperature(self):
        return self.temperature

    def get_fan_speed(self):
        return self.fan_speed

    def increase_fan_speed(self):
        if self.is_on:
            if self.fan_speed <= 5:
                self.fan_speed +=1
            else:
                self.fan_speed = 5
    def decrease_fan_speed(self):
        if self.is_on and self.fan_speed > 1:
            if self.fan_speed <= 5:
                self.fan_speed -=1
            else:
                self.fan_speed = 1








