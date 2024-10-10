from logging import raiseExceptions
from operator import truediv


class Television:

    def __init__(self):
        self.is_on: bool = False
        self.channel: int = 0
        self.volume_level: int = 0
        self.is_mute: bool = False
        self.previous_volume: int = 0

    def television_is_off(self):
         self.is_on = False

    def turn_on_television(self):
        self.is_on = True

    def television_is_on(self):
        return self.is_on

    def channel_up(self):
        if self.is_on == True and self.channel < 100:
            self.channel += 1
        else:
            raiseExceptions: 'television channel out of range or television is off'

    def channel_down(self):
        if self.is_on == True and self.channel >= 1:
            self.channel -= 1
        else:
            raiseExceptions: 'television channel out of range or television is off'

    def get_channel(self):
        return self.channel


    def set_channel(self, channel):
        if self.is_on == True and 0 <= self.channel <= 100:
            self.channel = self.channel


    def set_volume(self, volume):
        if self.is_on == True and 0 <= volume <= 100:
            self.volume_level = volume

    def get_volume(self):
        return self.volume_level

    def volume_up(self):
        if self.is_on == True and self.volume_level < 100:
            self.volume_level += 1
        else:
            raiseExceptions: 'television volume_level out of range or television is off'

    def volume_down(self):
        if self.is_on == True and self.volume_level >= 1:
            self.volume_level -= 1
        else:
            raiseExceptions: 'television volume_level out of range or television is off'

    def mute(self):
        if self.is_on:
            self.is_mute = True
            self.previous_volume = self.volume_level
            self.volume_level = 0

    def unmute(self):
        if self.is_on:
            self.is_mute = False
            self.volume_level = self.previous_volume


            





