import unittest
import automated_bike
from automated_bike.automatic_bike import Bike


class Bike_Test(unittest.TestCase):
    def setUp(self):
        self.bike = Bike()

    def test_bike_is_off(self):
        self.assertFalse(self.bike.bike_is_on())

    def test_bike_can_turn_on(self):
        self.bike.turn_on_bike()
        self.assertTrue(self.bike.bike_is_on())

    def test_bike_can_turn_off(self):
        self.bike.turn_on_bike()
        self.bike.turn_off_bike()
        self.assertFalse(self.bike.bike_is_on())

    def test_bike_is_on_gear_one(self):
        self.bike.turn_on_bike()

    def test_when_bike_is_on_gear_one_and_speed_0_bike_can_accelerates_to_speed_1(self):
        self.bike.turn_on_bike()
        self.bike.accelerate_in_gear_one()
        self.assertEqual(self.bike.get_bike_speed_level(), 1)

    def test_when_bike_is_on_gear_two_and_speed_21_bike_can_accelerates_to_speed_23(self):
        self.bike.turn_on_bike()
        self.bike.set_speed(21)
        self.bike.accelerate_in_gear_two()
        self.assertEqual(self.bike.get_bike_speed_level(), 23)

    def test_when_bike_is_on_gear_one_and_speed_15_bike_can_accelerates_to_speed_16(self):
        self.bike.turn_on_bike()
        self.bike.set_speed(15)
        self.bike.accelerate_in_gear_one()
        self.assertEqual(self.bike.get_bike_speed_level(),16)

    def test_when_bike_is_on_gear_three_and_speed_35_bike_can_accelerates_to_speed_38(self):
        self.bike.turn_on_bike()
        self.bike.set_speed(35)
        self.bike.accelerate_in_gear_three()
        self.assertEqual(self.bike.get_bike_speed_level(), 38)

    def test_when_bike_is_on_gear_four_and_speed_44_bike_can_accelerates_to_speed_48(self):
        self.bike.turn_on_bike()
        self.bike.set_speed(44)
        self.bike.accelerate_in_gear_four()
        self.assertEqual(self.bike.get_bike_speed_level(), 48)

    def test_when_bike_is_on_gear_one_and_speed_15_bike_can_decelerates_to_speed_14(self):
        self.bike.turn_on_bike()
        self.bike.set_speed(15)
        self.bike.decelerate_in_gear_one()
        self.assertEqual(self.bike.get_bike_speed_level(), 14)

    def test_when_bike_is_on_gear_two_and_speed_24_bike_can_decelerates_to_speed_22(self):
        self.bike.turn_on_bike()
        self.bike.set_speed(24)
        self.bike.decelerate_in_gear_two()
        self.assertEqual(self.bike.get_bike_speed_level(), 22)

    def test_when_bike_is_on_gear_three_and_speed_35_bike_can_decelerates_to_speed_32(self):
        self.bike.turn_on_bike()
        self.bike.set_speed(35)
        self.bike.decelerate_in_gear_three()
        self.assertEqual(self.bike.get_bike_speed_level(), 32)

    def test_when_bike_is_on_gear_four_and_speed_44_bike_can_decelerates_to_speed_40(self):
        self.bike.turn_on_bike()
        self.bike.set_speed(44)
        self.bike.decelerate_in_gear_four()
        self.assertEqual(self.bike.get_bike_speed_level(), 40)

    def test_when_bike_is_on_and_speed_is_above_20_bike_is_on_gear_two(self):
        self.bike.turn_on_bike()
        self.bike.set_speed(22)
        self.assertEqual(self.bike.get_current_gear(), 2)

    def test_when_bike_is_on_and_speed_is_above_zero_but_less_than_twenty_bike_is_on_gear_one(self):
        self.bike.turn_on_bike()
        self.bike.set_speed(15)
        self.assertEqual(self.bike.get_current_gear(), 1)

    def test_when_bike_is_on_and_speed_is_above_thirty_bike_is_on_gear_three(self):
        self.bike.turn_on_bike()
        self.bike.set_speed(36)
        self.assertEqual(self.bike.get_current_gear(), 3)

    def test_when_bike_is_on_and_speed_is_above_forty_bike_is_on_gear_four(self):
        self.bike.turn_on_bike()
        self.bike.set_speed(52)
        self.assertEqual(self.bike.get_current_gear(), 4)

    def test_when_bike_is_on_speed_cannot_decelerate_below_zero(self):
        self.bike.turn_on_bike()
        self.bike.decelerate_in_gear_one()
        self.assertEqual(self.bike.get_bike_speed_level(), 0)



if __name__ == '__main__':
    unittest.main()
