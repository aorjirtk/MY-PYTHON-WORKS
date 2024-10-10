class Bike:

    def __init__(self):
        self.is_on:bool = False
        self.gear:int = 1
        self.speed:int = 0

    def bike_is_on(self):
            return self.is_on

    def turn_off_bike(self):
         self.is_on = False

    def turn_on_bike(self):
        self.is_on = True

    def get_current_gear(self):
        if self.is_on:
            if 0 <= self.speed <= 20:
                self.gear = 1
            elif 21 <= self.speed <= 30:
                self.gear = 2
            elif 31 <= self.speed <= 40:
                self.gear = 3
            elif self.speed >= 41:
                self.gear = 4
            return self.gear

    def set_speed(self, speed):
        if self.is_on:
            if self.speed >= 0 and  speed <= 100:
                self.speed = speed

    def accelerate_in_gear_one(self):
        if self.is_on:
            if self.speed < 20:
                self.speed += 1
            else:
                self.speed = self.speed

    def accelerate_in_gear_two(self):
        if self.is_on:
            if 21 <= self.speed <= 30:
                self.speed += 2
            else:
                self.speed = self.speed

    def accelerate_in_gear_three(self):
        if self.is_on:
            if 31 <= self.speed <= 40:
                self.speed += 3
            else:
                self.speed = self.speed

    def accelerate_in_gear_four(self):
        if self.is_on:
            if self.speed >= 41:
                self.speed += 4

    def get_bike_speed_level(self):
            return self.speed

    def decelerate_in_gear_one(self):
        if self.is_on and self.speed > 0:
            if 1 <= self.speed <= 20:
                self.speed -= 1

    def decelerate_in_gear_two(self):
        if self.is_on and self.speed > 20:
            if 22 <= self.speed <= 30:
                self.speed -= 2

    def decelerate_in_gear_three(self):
        if self.is_on and self.speed > 30:
            if 33 <= self.speed <= 40:
                self.speed -= 3

    def decelerate_in_gear_four(self):
        if self.is_on and self.speed > 40:
            if self.speed >= 44:
                self.speed -= 4




